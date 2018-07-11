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
from random import random, shuffle, choice
from container import PriorityQueue


class Scheduler:
    """A scheduler, capable of deciding what parcels go onto which trucks, and
    what route each truck will take.

    This is an abstract class.  Only child classes should be instantiated.

    You may add *private* methods to this class so make them available to both
    subclasses.
    """
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
    def __init__(self,parcels,trucks):
        self.parcels = parcels
        self.trucks = trucks

    def schedule(self, parcels,trucks,verbose = False):
        #organizes the parcels using random algorithm
        copy_p = self.parcels[:]
        i = 0
        not_scheduled = []
        while i <len(self.parcels):
            l = random.choice(copy_p)
            s = random.choice(trucks)
            if s.check ==True:
                s.add(l)
            else:
                not_scheduled.append(l)
            copy_p.remove(l)
            i = i + 1
        return not_scheduled


class GreedyScheduler(Scheduler):
    def __init__(self,parcels,trucks):
        self.parcels = parcels
        self.trucks = trucks

    def increasing_volume(self,parcels):
        # returns a list of parcels in increasing volume
        inc_volume = []
        copy_parcels = self.parcels[:]
        not_scheduled = []
        for parcel in copy_parcels:
            inc_volume.append(parcel.parcel_volume)
        i = 0
        new_lst = []
        while i <len(self.parcels):
            index =  inc_volume.index(max(inc_volume))
            new_lst.append(copy_parcels.pop(index))
            inc_volume.remove(index)
            i = i+1

        return new_lst


    def decreasing_volume(self,parcels):
        # returns a list of parcels in decreasing volume
        inc_volume = []
        copy_parcels = self.parcels[:]
        for parcel in copy_parcels:
            inc_volume.append(parcel.parcel_volume)

        i = 0
        new_lst = []
        while i < len(self.parcels):
            index = inc_volume.index(min(inc_volume))
            new_lst.append(copy_parcels.pop(index))
            inc_volume.remove(index)
            i = i + 1
        return

    def increasing_des(self,parcels):
        # returns a list of parcels in increasing destination alphabetically
        inc_volume = []
        copy_parcels = self.parcels[:]
        for parcel in copy_parcels:
            inc_volume.append(parcel.destination)

        i = 0
        new_lst = []
        while i < len(self.parcels):
            index = inc_volume.index(max(inc_volume))
            new_lst.append(copy_parcels.pop(index))
            inc_volume.remove(index)
            i = i + 1
        return new_lst

    def decreasing_des(self,parcels):
        # returns a list of parcels in decreasing destination alphabetically
        inc_volume = []
        copy_parcels = self.parcels[:]
        for parcel in copy_parcels:
            inc_volume.append(parcel.parcel_volume)

        i = 0
        new_lst = []
        while i < len(self.parcels):
            index = inc_volume.index(min(inc_volume))
            new_lst.append(copy_parcels.pop(index))
            inc_volume.remove(index)
            i = i + 1
        return new_lst

    def eligible_trucks(self,item):
        # returns a list of elgible trucks that an item can fit into
        eligible_tr = []
        route_tr = []
        for truck in self.trucks:
            if truck.volume_cap>=item.parcel_volume:
                eligible_tr.append(truck)
        for truck in eligible_tr:
            if truck.same_route(item):
                route_tr.append(truck)
        if route_tr == []:
            return eligible_tr
        else:
            return route_tr

    def least_vol(self,eligible_tr):
        # returns a truck with least vol from all eligble trucks
        inc_volume = []
        for truck in eligible_tr:
            inc_volume.append(truck.volume_cap)

        index = inc_volume.index(min(inc_volume))
        return elgible_tr[index]

    def max_vol(self,eligible_tr):
        # returns a truck with max vol from all eligible trucks
        inc_volume = []
        for truck in eligible_tr:
            inc_volume.append(truck.volume_cap)

        index = inc_volume.index(max(inc_volume))
        return elgible_tr[index]































        for parcel in self.parcels:
            if parcel.parcel_volume[i]<parcel.parcel_volume[i+1]:
                break
            i = i+ 1


    def increasing_parcel(self,parcels):
        i = o
        while len(self.parcels)>i:
            if self.parcels[i]>self.parcels[i+1]:
                self.parcels.insert(self.parcels[i+1],self.parcels[i])
                break
            i = i+1


















# TODO: Implement classes RandomScheduler and GreedyScheduler.


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config='.pylintrc')
