"""Assignment 2: Trees for Treemap

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains the basic tree interface required by the treemap
visualiser. You will both add to the abstract class, and complete a
concrete implementation of a subclass to represent files and folders on your
computer's file system.
"""
import os
from random import randint
import math


class AbstractTree:
    """A tree that is compatible with the treemap visualiser.

    This is an abstract class that should not be instantiated directly.

    You may NOT add any attributes, public or private, to this class.
    However, part of this assignment will involve you adding and implementing
    new public *methods* for this interface.

    === Public Attributes ===
    @type data_size: int
        The total size of all leaves of this tree.
    @type colour: (int, int, int)
        The RGB colour value of the root of this tree.
        Note: only the colours of leaves will influence what the user sees.

    === Private Attributes ===
    @type _root: obj | None
        The root value of this tree, or None if this tree is empty.
    @type _subtrees: list[AbstractTree]
        The subtrees of this tree.
    @type _parent_tree: AbstractTree | None
        The parent tree of this tree; i.e., the tree that contains this tree
        as a subtree, or None if this tree is not part of a larger tree.

    === Representation Invariants ===
    - data_size >= 0
    - If _subtrees is not empty, then data_size is equal to the sum of the
      data_size of each subtree.
    - colour's elements are in the range 0-255.

    - If _root is None, then _subtrees is empty, _parent_tree is None, and
      data_size is 0.
      This setting of attributes represents an empty tree.
    - _subtrees IS allowed to contain empty subtrees (this makes deletion
      a bit easier).

    - if _parent_tree is not empty, then self is in _parent_tree._subtrees
    """
    def __init__(self, root, subtrees, data_size=0):
        """Initialize a new AbstractTree.

        If <subtrees> is empty, <data_size> is used to initialize this tree's
        data_size. Otherwise, the <data_size> parameter is ignored, and this tree's
        data_size is computed from the data_sizes of the subtrees.

        If <subtrees> is not empty, <data_size> should not be specified.

        This method sets the _parent_tree attribute for each subtree to self.

        A random colour is chosen for this tree.

        Precondition: if <root> is None, then <subtrees> is empty.

        @type self: AbstractTree
        @type root: object
        @type subtrees: list[AbstractTree]
        @type data_size: int
        @rtype: None
        """
        self._root = root
        self._subtrees = subtrees
        self._parent_tree = None
        self.data_size = data_size

        for n in self._subtrees:
            n.data_size = os.path.getsize(n)
            self.data_size += os.path.getsize(n)
            n._parent_tree = self

        self.colour = (randint(0, 255), randint(0, 255), randint(0, 255))

    def is_empty(self):
        """Return True if this tree is empty.

        @type self: AbstractTree
        @rtype: bool
        """
        return self._root is None

    def generate_treemap(self, rect):
        """Run the treemap algorithm on this tree and return the rectangles.

        Each returned tuple contains a pygame rectangle and a colour:
        ((x, y, width, height), (r, g, b)).

        One tuple should be returned per non-empty leaf in this tree.

        @type self: AbstractTree
        @type rect: (int, int, int, int)
            Input is in the pygame format: (x, y, width, height)
        @rtype: list[((int, int, int, int), (int, int, int))]


        """
        # return empty list if tree is empty
        treemap = []
        if self._root is None:
            return []

        # return rect and the colour of the rectangle for a tree w/just root
        if self._subtrees is None:
            treemap.append((rect, self.colour))
            return treemap

        # recursion
        height = rect[3]
        width = rect[2]
        x = rect[0]
        y = rect[1]
        for subtree in self._subtrees:
            percent = int((subtree.data_size/self.data_size)*100)
            if width < height:
                temp_width = int(width*(percent/100))
                temp = (x, y, temp_width, height)
                treemap.append((temp, subtree.colour))
                x += width
                subtree.generate_treemap(temp)
            elif height >= width:
                temp_height = int(height*(percent/100))
                temp = (x, y, width, temp_height)
                y += height
                treemap.append((temp, subtree.colour))
                subtree.generate_treemap(temp)

    def get_separator(self):
        """Return the string used to separate nodes in the string
        representation of a path from the tree root to a leaf.

        Used by the treemap visualiser to generate a string displaying
        the items from the root of the tree to the currently selected leaf.

        This should be overridden by each AbstractTree subclass, to customize
        how these items are separated for different data domains.

        @type self: AbstractTree
        @rtype: str
        """
        raise NotImplementedError


class FileSystemTree(AbstractTree):
    """A tree representation of files and folders in a file system.

    The internal nodes represent folders, and the leaves represent regular
    files (e.g., PDF documents, movie files, Python source code files, etc.).

    The _root attribute stores the *name* of the folder or file, not its full
    path. E.g., store 'assignments', not '/Users/David/csc148/assignments'

    The data_size attribute for regular files as simply the size of the file,
    as reported by os.path.getsize.
    """
    def __init__(self, path):
        """Store the file tree structure contained in the given file or folder.

        Precondition: <path> is a valid path for this computer.

        @type self: FileSystemTree
        @type path: str
        @rtype: None
        """
        AbstractTree.__init__(self, root=None, subtrees=[])
        if os.path.isfile(path):  # if path is just one file
            self._subtrees = []
            self._root = os.path.basename(path)
            self.data_size = os.path.getsize(path)
            return

        else:  # path is more than just one file
            base = os.path.basename(path)
            folders = os.listdir(path)
            AbstractTree.__init__(self, base, [])
            for subtree in folders:
                newpath = os.path.join(path, subtree)
                newtree = FileSystemTree(newpath)
                self._subtrees.append(newtree)
                newtree._parent_tree = self
                self.data_size += newtree.data_size


    def is_empty(self):
        """

        :return:
        :rtype:
        """
        pass




    def generate_treemap(self, rect):
        """Run the treemap algorithm on this tree and return the rectangles.

        Each returned tuple contains a pygame rectangle and a colour:
        ((x, y, width, height), (r, g, b)).

        One tuple should be returned per non-empty leaf in this tree.

        @type self: AbstractTree
        @type rect: (int, int, int, int)
            Input is in the pygame format: (x, y, width, height)
        @rtype: list[((int, int, int, int), (int, int, int))]


        """
        # return empty list if tree is empty

        treemap = []
        if self._root is None:
            return []

        # return rect and the colour of the rectangle for a tree w/just root
        # if item is just file
        if self._subtrees == []:
            treemap.append((rect, self.colour))
            return treemap

        # recursion
        height = rect[3]
        width = rect[2]
        x = rect[0]
        y = rect[1]

        for subtree in self._subtrees:
            if subtree._subtrees == []:
                percent = math.floor((subtree.data_size/self.data_size)*100)
                if width < height:
                    temp_height = math.floor(height*(percent/100)) #
                    temp = (x, y, width, temp_height)
                    treemap.append((temp, subtree.colour))
                    y += temp_height
                    #subtree.generate_treemap(temp)

                else:
                    temp_width = int(width*(percent/100))
                    temp = (x, y, temp_width, height)
                    x += temp_width
                    treemap.append ((temp, subtree.colour))
                   # subtree.generate_treemap(temp)
            else:
                child_start_height = rect[0]
                child_start_width = rect[1]
                for subtree in self._subtrees:
                    percent = math.floor((subtree.data_size / self.data_size) * 100)
                    child_subtree_height = percent /100 * (height)
                    child_subtree_width = percent / 100 * (width)
                    if height < width:
                        child_start_width += child_subtree_width
                    else:
                        child_start_height += child_subtree_height

                    newrect = (child_start_height,child_start_width,child_subtree_height,child_subtree_width)
                    subtree.generate_treemap(newrect)

        return treemap

    def get_separator(self):
        """

        :return:
        :rtype:
        """
        pass

'''
if __name__ == '__main__':
    import python_ta
    # Remember to change this to check_all when cleaning up your code.
    python_ta.check_errors(config='pylintrc.txt')


test_tree = FileSystemTree('/home/quinn/Dropbox/148 A2/example-data/')
print(len(test_tree._subtrees))
beta = test_tree.generate_treemap((0,0,0,0))
'''