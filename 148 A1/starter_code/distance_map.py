"""Assignment 1 - Distance map (Task 1)

This module contains the class DistanceMap, which is used to store and lookup
distances between cities.  This class does not read distances from the map file.
All reading from files is done in module experiment.

Your task is to design and implement this class.

Do not import any modules here.
"""


class DistanceMap:
    """A map of distances between cities
    """

    def __init__(self,fromcity,tocity,dvalue):
        """Initializes a DistanceMap object
        @type fromcity: City
        @type tocity: City
        @type dvalue: int
        @rtype: None
        """
        self.fromcity = fromcity
        self.tocity = tocity
        self.dvalue = dvalue
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config='.pylintrc')
