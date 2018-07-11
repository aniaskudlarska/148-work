from tree_data import AbstractTree
import os
import sys
class FileSystemTree(AbstractTree):

    def __init__(self,path):

        if path is None:
            self._root, self._subtrees = None

        AbstractTree.__init__(self,root=None, subtrees=[])
        new_path = path.split('/')
        if len(new_path) == 1:
            self._root = os.path.basename(path)
            self._subtrees = []
        else:
            self._root = os.path.basename(path)
            self._subtrees = new_path[2:]

        total_data = 0
        for tree in self._subtrees:
            tree_size = os.path.getsize(tree)
            tree.data_size = tree_size
            total_data += tree_size
        self.data_size = total_data



sys.getsizeof(x)