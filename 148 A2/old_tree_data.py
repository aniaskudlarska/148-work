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
import sys


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
    @type _root:  obj | None
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
        # 2. Properly set all _parent_tree attributes in self._subtrees
        for n in self._subtrees:
            n._parent_tree = self

        # 1. Initialize self.colour and self.data_size, according to the docstring.
        self.colour = (randint(0, 255),
                      randint(0, 255),
                      randint(0, 255)) #rgb tuple

        if self.is_empty(): #initialize data size
            self.data_size = data_size #0

        if not self.is_empty(): #calculate data size from subtrees
            total_data = 0
            for tree in self._subtrees:
                tree_size = os.path.getsize(tree)
                total_data += tree_size

    def is_empty(self):
        """Return True if this tree is empty.

        @type self: AbstractTree
        @rtype: bool
        """
        return self._root is None

    def find_data_size(self):
        """
        Returns the data size of the Abstract Tree

        @type self: AbstractTree
        @rtype: int
        """

        if not os.path.isdir(self):
            return os.path.getsize(self)
        else:
            count = 0
            for subtree in self._subtrees:
                count += subtree.find_data_size()
            self.data_size = count
            return count

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
        # TODO: implement this method!
        # Read the handout carefully to help get started identifying base cases,
        # and the outline of a recursive step.
        #
        # Programming tip: use "tuple unpacking assignment" to easily extract
        # coordinates of a rectangle, as follows.
        # x, y, width, height = rect
        pass

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
        # Remember that you should recursively go through the file system
        # and create new FileSystemTree objects for each file and folder
        # encountered.
        #
        # Also remember to make good use of the superclass constructor!
        def find_data_size(path):
            """
            Returns the data size of the Abstract Tree

            @type self: str
            @rtype: int
            """
            Tree = FileSystemTree(path)
            if not os.path.isdir(path):
                return os.path.getsize(path)
            else:
                count = 0
                for subtree in Tree._subtrees:
                    count += subtree.find_data_size()
                Tree.data_size = count
                return count

        AbstractTree.__init__(self, root= None, subtrees=[])
        if os.path.isfile(path):
            self._subtrees = []
            self._root = os.path.basename(path)
            return

        folderlist = os.listdir(path)
        self._root = os.path.basename(path)

        self._subtrees = []

        for n in folderlist:
            n_path = os.path.join(path,n)
            if os.path.isdir(n_path):
                newtree = FileSystemTree(n_path)
                self._subtrees.append(newtree)

        total_data = find_data_size(self)
        self.data_size = total_data




'''
if __name__ == '__main__':
    import python_ta
    # Remember to change this to check_all when cleaning up your code.
    python_ta.check_errors(config='pylintrc.txt')
'''
x = FileSystemTree('/home/quinn/test')
for y in x._subtrees:
    if isinstance(y,FileSystemTree):
        print(y._root)
    else:
        print(y)
    ### test cases
