"""Assignment 1 - Running experiments (Tasks 5 & 6)

This module contains class SchedulingExperiment.  It can create an experiment
with input data and an algorithm configuration specified in a dictionary, then
run the experiment, generate statistics as the result of the experiment, and
(optionally) report the statistics.

This module is responsible for all the reading of data from the data files.

To test your code, we will construct instances of SchedulingExperiment, call
its methods, and examine the dictionary of statistics that method run
returns.

If you defined any domain classes other than Parcel and Truck, you may import
them here.  You may not import external libraries.
"""
from scheduler import RandomScheduler, GreedyScheduler
from domain import Parcel, Truck
from distance_map import DistanceMap
from container import *

class SchedulingExperiment:
    """An experiment in scheduling parcels for delivery.

    To complete an experiment involves four stages:

    1. Read in all data from necessary files, and create corresponding objects.
    2. Run a scheduling algorithm to assign parcels to trucks.
    3. Compute statistics showing how good the assignment of parcels to trucks
       is.
    4. Report the statistics from the experiment.

    #All strs point to filenames
    :type config: dict
    :type depot: str
    :type truckfile: str
    :type mapfile: str
    :type parcelfile: str
    :type algorithm: str
    :type parcel_priority: str
    :type truck_order: str
    :type verbose: str
    """
    def __init__(self, config):
        """Initialize a new experiment from a configuration dictionary.

        Precondition: <config> contains keys and values as specified
        in Assignment 1.

        @type config: dict[str, str]
            The configuration for this experiment, including
            the data files and algorithm configuration to use.
        @rtype: None
        """
        self.config = {}
        with open(config, 'r') as file:
            for line in file:
                split = line.split(":")
                key = split[0]
                data = split[1]
                self.config['key'] = data
        self.depot = self.config["depot_location"]
        self.truckfile = self.config["truck_file"]
        self.mapfile = self.config["map_file"]
        self.parcelfile = self.config["parcel_file"]
        self.algorithm = self.config["algorithm"]
        self.parcel_priority = self.config["parcel_priority"]
        self.parcel_order = self.config["parcel_order"]
        self.truck_order = self.config["truck_order"]
        self.verbose = self.config["verbose"]
        pass

    def run(self, report=False):
        """Run the experiment and return statistics on the outcome.

        If <report> is True, print a report on the statistics from this
        experiment.  Either way, return the statistics in a dictionary.

        If <self.verbose> is True, print step-by-step details
        regarding the scheduling algorithm as it runs.

        @type self: SchedulingExperiment
        @type report: bool
            Whether or not to print a report on the statistics.
        @rtype: dict[str, int | float]
            Statistics from this experiment. Keys and values are as specified
            in Step 6 of Assignment 1.
        """
        ## STEP ZERO: BUILD LISTS OF STUFF TO USE ##
        Trucklist = read_trucks(self.truckfile,self.depot)
        Maplist = read_distance_map(self.mapfile)
        Parcellist = read_parcels(self.parcelfile)

        ## STEP ONE: PROCESS PARCELS, THEN PROCESS TRUCKS - 8 ORDERS TOTAL ##
        ## buckle up this is gonna get messy
        if self.parcel_priority == "volume" and self.parcel_order == "non-decreasing":
            whichalgorithm = 1
            if self.truck_order == "non-decreasing":
                # ADD TRUCKS TO A PRIORITY QUEUE IN ORDER OF INCREASING SPACE REMAINING
                for truck in Trucklist:
                    TruckQueue = PriorityQueue(less_than=not(less_than_truck_volume(truck,truck)))
                    TruckQueue.add(truck)

            if self.truck_order == "decreasing":
                # ADD TRUCKS TO A PRIORITY QUEUE IN ORDER OF DECREASING SPACE REMAINING
                TruckQueue = PriorityQueue
                for truck in Trucklist:
                    TruckQueue = PriorityQueue(less_than=(less_than_truck_volume(truck, truck)))
                    TruckQueue.add(truck)

        if self.parcel_priority == "destination" and self.parcel_order == "non-decreasing":
            whichalgorithm = 2
            if self.truck_order == "non-decreasing":
                for truck in Trucklist:
                    TruckQueue = PriorityQueue(less_than=not (less_than_truck_volume(truck, truck)))
                    TruckQueue.add(truck)
            if self.truck_order == "decreasing":
                for truck in Trucklist:
                    TruckQueue = PriorityQueue(less_than=(less_than_truck_volume(truck, truck)))
                    TruckQueue.add(truck)

        if self.parcel_priority == "volume" and self.parcel_order == "decreasing":
            whichalgorithm = 3
            if self.truck_order == "non-decreasing":
                for truck in Trucklist:
                    TruckQueue = PriorityQueue(less_than=not (less_than_truck_volume(truck, truck)))
                    TruckQueue.add(truck)

            if self.truck_order == "decreasing":
                for truck in Trucklist:
                    TruckQueue = PriorityQueue(less_than=(less_than_truck_volume(truck, truck)))
                    TruckQueue.add(truck)

        if self.parcel_priority == "destination" and self.parcel_order == "decreasing":
            whichalgorithm = 4
            if self.truck_order == "non-decreasing":
                for truck in Trucklist:
                    TruckQueue = PriorityQueue(less_than=not (less_than_truck_volume(truck, truck)))
                    TruckQueue.add(truck)

            if self.truck_order == "decreasing":
                for truck in Trucklist:
                    TruckQueue = PriorityQueue(less_than=(less_than_truck_volume(truck, truck)))
                    TruckQueue.add(truck)

        ## STEP TWO - ALGORITHIM
        ## Selects which of the 4 parcel algorithims to use, if greedy, or just random, if random

        if self.algorithm == "greedy":
            #do greedy stuff
            Scheduler = GreedyScheduler(Parcellist,Trucklist)
            if whichalgorithm == 1:
                Sorted_Parcels = Scheduler.decreasing_volume(Parcellist)
                Sorted_Parcels2 = Scheduler.increasing_des(Sorted_Parcels)

            if whichalgorithm == 2:
                Sorted_Parcels = Scheduler.increasing_volume(Parcellist)
                Sorted_Parcels2 = Scheduler.increasing_des(Sorted_Parcels)

            if whichalgorithm == 3:
                Sorted_Parcels = Scheduler.decreasing_volume(Parcellist)
                Sorted_Parcels2 = Scheduler.decreasing_des(Parcellist)

            if whichalgorithm == 4:
                Sorted_Parcels = Scheduler.increasing_volume(Parcellist)
                Sorted_Parcels2 = Scheduler.decreasing_des(Parcellist)


        if self.algorithm == "random":
            # do random stuff
            Scheduler = RandomScheduler(Parcellist,Trucklist)
            unused_trucks = Scheduler.schedule(parcels=Parcellist, trucks=Trucklist)

        #build some lists so other functions can use them
        self.unused = unused_trucks
        self.trucklist = Trucklist
        return self._compute_stats()

    def _compute_stats(self):
        """Compute the statistics for this experiment.

        Precondition: _run has already been called.

        @type self: SchedulingExperiment
        @rtype: Dict[str, int | float]
            Statistics from this experiment. Keys and values are as specified
            in Step 6 of Assignment 1.
        """

        statdic = {} #Dictionary of all the statistics, with keys as str and values as int
        statdic['fleet'] = len(read_trucks(self.truckfile,self.depot))
        statdic['unused_trucks'] = len(self.unused)
        statdic['avg_distance'] =  sum(read_distance_map(distance_map_file=self.mapfile)) / statdic['fleet']
        statdic['avg_fullness'] = total_space(self.Trucklist) / statdic['fleet']
        statdic['unused_space'] = remaining_space(self.Trucklist)/ statdic['fleet']
        statdic['unscheduled'] = len(self.unused)

        return statdic


    def _print_report(self):
        """Report on the statistics for this experiment.

        This method is *only* for debugging purposes for your benefit, so
        the content and format of the report is your choice; we
        will not call your run method with <report> set to True.

        Precondition: _compute_stats has already been called.

        @type self: SchedulingExperiment
        @rtype: None
        """

        for key in self._compute_stats():
            print(key)
            for value in key:
                print(value)


# ----- Helper functions -----

def total_space(Trucklist):
    """returns total space of a list of trucks
    @type Trucklist: list
    @rtype: int
    """
    n = 0
    for truck in Trucklist
        n += truck.volume_cap

    return n

def remaining_space(Trucklist):
    """returns unused space in trucks
    @type Trucklist: list
    @rtype: int
    """
    n = 0
    for truck in Trucklist:
        n += truck.volume_cap - truck.storage
    return n

## for the Queue
def less_than_parcel(p1,p2):
    """compare the volume of two parcels
    @type p1: Parcel
    @type p2: Parcel
    @rtype: bool
    """
    return p1.parcel_volume < p2.parcel_volume

def less_than_truck_volume(t1,t2):
    """compare the remaining volume of two trucks
    @type t1: Truck
    @type t2: Truck
    @rtype: bool
    """
    for item in t1.storage:
        return t1.volume_cap-item.parcel_volume < t2.volume_cap-item.parcel_volume

def read_parcels(parcel_file):
    """Read parcel data from <parcel_file> and return XXXX

    @type parcel_file: str
        The name of a file containing parcel data in the form specified in
        Assignment 1.
    @rtype: list

    >>>print(read_parcels("data"))
    >>>'[list of things in that data file]'
    """
    parcellist = []

    with open(parcel_file, 'r') as file:
        for line in file:
            tokens = line.strip().split(',')
            pid = int(tokens[0].strip())
            source = tokens[1].strip()
            destination = tokens[2].strip()
            volume = int(tokens[3].strip())
            parcel = Parcel(pid,source,destination,volume)
            parcellist.append(parcel)
    return parcellist



def read_distance_map(distance_map_file):
    """Read distance data from <distance_map_file> and return XXXX

    @type distance_map_file: str
        The name of a file containing distance data in the form specified in
        Assignment 1.
    @rtype: list

    """
    citylist = []

    with open(distance_map_file, 'r') as file:
        for line in file:
            tokens = line.strip().split(',')
            c1 = tokens[0].strip()
            c2 = tokens[1].strip()
            dist = int(tokens[2].strip())
            citymap = DistanceMap(c1,c2,dist)
            citylist.append(citymap)
    return citylist

def read_trucks(truck_file, depot_location):
    """Read truck data from <truck_file> and return XXXX

    @type truck_file: str
        The name of a file containing truck data in the form specified in
        Assignment 1.
    @type depot_location: str
        The city where all the trucks (and packages) are at the start of the
        experiment.
    @rtype: list

    TODO: Complete this docstring.
    """
    trucklist = []
    with open(truck_file, 'r') as file:
        for line in file:
            tokens = line.strip().split(',')
            tid = int(tokens[0])
            capacity = int(tokens[1])
            truck = Truck(tid,capacity)
            trucklist.append(truck)

    return trucklist


def sanity_check(config_file):
    """Configure and run a single experiment on the scheduling problem
    defined in <config_file>

    Precondition: <config_file> is a json file with keys and values
    as in the dictionary format defined in Assignment 1.

    @type config_file: str
    @rtype: None
    """
    # Read an experiment configuration from a file and build a dictionary
    # from it.
    import json
    with open(config_file, 'r') as file:
        configuration = json.load(file)
    # Create and run an experiment with that configuration.
    experiment = SchedulingExperiment(configuration)
    experiment.run(report=True)

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='.pylintrc')

    # ------------------------------------------------------------------------
    # The following code can be used as a quick and dirty check to see if your
    # experiment can run without errors. Feel free to uncomment it for testing
    # purposes, but you should remove it before submitting your final version.
    # ------------------------------------------------------------------------
    # sanity_check('data/demo.json')
