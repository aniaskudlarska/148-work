"""Assignment 1 - Domain classes (Task 2)

This module contains all of the classes required to represent the entities
in the experiment, including at least a class Parcel and a class Truck.
"""

# TODO: Implement class Parcel, class Truck, and perhaps other classes to
# represent the entities in the experiment..

class Parcel:
    def __init__(self, parcel_id, source, destination, parcel_volume):
        self.parcel_id = parcel_id
        self.source = source
        self.destination = destination
        self.parcel_volume = parcel_volume


class Truck:
    def __init__(self, truck_id, volume_cap):
        """
        :type truck_id : str
        :type item:Parcel
        :type volume_cap:int
        """
        if volume_cap > 0:
            self.volume_cap = volume_cap
            self.truck_id = truck_id
            self.storage = []
            self.routes = []

    def add_parcel(self, item):
        self.volume_cap = self.volume_cap - item.parcel_volume
        self.storage.append(item)
        self.routes.append(item.destination)
    def same_route(self,item):
        if item.distination in self.routes:
            return True


    def check(self, item):
        if item.parcel_volume <= self.volume_cap:
            return True
        else:
            return False
if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='.pylintrc')
    import doctest
    doctest.testmod()
