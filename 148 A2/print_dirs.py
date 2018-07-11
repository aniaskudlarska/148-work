import os


def print_items(d, indentation):
    """A sample program showing how to recurse on directories using os.

    Print the list of files and directories in directory <d>, recursively,
    prefixing each with the given indentation.

    @type d: str
    @type indentation: str
    @rtype: None
    """
    print(indentation + d + ':')
    for filename in os.listdir(d):
        print(indentation + filename)
        subitem = os.path.join(d, filename)
        if os.path.isdir(subitem):
            print_items(subitem, indentation + '    ')


if __name__ == '__main__':
    # Put in a path like
    # 'C:\\Users\\David\\Documents\\csc148\\assignments' (Windows) or
    # '/Users/dianeh/Documents/courses/csc148/assignments' (OSX)
    # to print the contents of that folder.
    print_items('C:\\test1\\test2\\test3', '')
