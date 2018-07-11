"""Assignment 1 - Scheduling algorithms (Task 4)

This module contains the abstract Scheduler interface, as well as the two
classes RandomScheduler and GreedyScheduler, which implement the two
scheduling algorithms described in the handout.

Your task is to implement RandomScheduler and GreedyScheduler.
You may *not* change the public interface of these classes, except that
you must write appropriate constructors for them.  The two constructors do not
need to have the same signatures.

Any attributes you use must be private, so that the public interface is exactly
what is specified by the Scheduler abstract class.
"""
from random import shuffle, choice
from container import PriorityQueue


class Scheduler:
    """A scheduler, capable of deciding what parcels go onto which trucks, and
    what route each truck will take.

    This is an abstract class.  Only child classes should be instantiated.

    You may add *private* methods to this class so make them available to both
    subclasses.
    """
    def __init__(self,parcels,trucks,distance_map):
        self.parcels = parcels
        self.trucks = trucks
        self.distance_map = distance_map

    def schedule(self, parcels, trucks, verbose=False):
        """Schedule the given parcels onto the given trucks.

        Mutate the trucks so that they store information about which
        parcels they will deliver and what route they will take.
        Do *not* mutate the parcels.

        Return the parcels that do not get scheduled onto any truck, due to
        lack of capacity.

        If <verbose> is True, print step-by-step details regarding
        the scheduling algorithm as it runs.  This is *only* for debugging
        purposes for your benefit, so the content and format of this
        information is your choice; we will not test your code with <verbose>
        set to True.

        @type self: Scheduler
        @type parcels: list[Parcel]
            The parcels to be scheduled for delivery.
        @type trucks: list[Truck]
            The trucks that can carry parcels for delivery.
        @type verbose: bool
            Whether or not to run in verbose mode.
        @rtype: list[Parcel]
            The parcels that did not get scheduled onto any truck, due to
            lack of capacity.
        """
        raise NotImplementedError

class RandomScheduler(Scheduler):

        def schedule(self,parcels,trucks,verbose=False):
            immovable_parcels = []

            for parcel in parcels:
                eligible_trucks = []
                for truck in trucks:
                    if truck.truck_volume >= parcel.parcel_volume: #finds trucks with enough cargo space
                        eligible_trucks.append(truck) #builds a list of eligible trucks
                choice(eligible_trucks).cargo.append(parcel) #choice finds a random object and adds the parcel to that object

            for parcel in parcels:
                for truck in trucks:
                    if not parcel.is_in_truck(truck):
                        immovable_parcels.append(parcel)
            return immovable_parcels

class GreedyScheduler(Scheduler):

    def schedule(self,parcels,trucks,verbose=False):
        immovable_parcels = []
        for parcel in parcels:
            eligible_trucks = []
            for truck in trucks:
                if truck.truck_volume >= parcel.parcel_volume:
                    eligible_trucks.append(truck)


# TODO: Implement classes RandomScheduler and GreedyScheduler.


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config='.pylintrc')
