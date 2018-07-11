"""Assignment 1 - Domain classes (Task 2)

This module contains all of the classes required to represent the entities
in the experiment, including at least a class Parcel and a class Truck.
"""

# TODO: Implement class Parcel, class Truck, and perhaps other classes to
# represent the entities in the experiment..

class Parcel:
    def __init__(self,parcel_id,source,destination,parcel_volume):
        """initializes a parcel
        @type parcel_id: str
        @type source: str
        @type destination: str
        @type parcel_volume: int
        """
        self.parcel_id = parcel_id
        self.source = source
        self.destination = destination
        self.parcel_volume = parcel_volume

    def is_in_truck(self,Truck):
        """returns True if parcel is in the specified truck
        """
        for element in Truck.cargo:
            if element == self:
                return True
        return False

class Truck:
    """Initializes a Truck
    @type truck_id: str
    @type truck_volume: int
    """
    def __init__(self,truck_id,truck_volume,cargo):
        if cargo <= truck_volume:
            self.truck_id = truck_id
            self.truck_volume = truck_volume - cargo
            self.cargo = cargo

'''
class City:
    def __init__(self):
        pass
'''

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='.pylintrc')
    import doctest
    doctest.testmod()
