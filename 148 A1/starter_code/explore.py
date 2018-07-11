"""Assignment 1 - Explore and compare all algorithms on a single problem.

This module reads from a json file (whose name is hard-coded in the main block)
to determine the parcel, truck and map files to use.  It then constructs all
nine possible algorithm configurations, and runs each on on this same data.
Results are printed to a csv file called 'results.csv'.

You have no tasks associated with this module.  It is provided to you so that
you can compare the performance of the algorithms and notice any patterns or
conclusions you might draw.  You may also find that reviewing the comparison
reveals bugs in your code.
"""

import json
from experiment import SchedulingExperiment


def print_table_title(file):
    """Print the title row of a results table, in csv format.

    @type file: file
        The file to write to.
    @rtype: None
    """
    file.write('Algorithm,Parcel Priority,Parcel Order,Truck Order,' +
               'Unused Trucks,Unused Space,Avg dist,Avg fullness,' +
               'Unsched Parcels\n')


def print_table_row(config, stats, file):
    """Print one row of a results table, in csv format.

    @type config: Dict[str, str]
        The configuration that was used.
    @type stats: Dict[str, int | float]
        The stats that resulted.
    @type file: file
        The file to write to.
    @rtype: None
    """
    file.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n' %
               (config['algorithm'],
                config['parcel_priority'],
                config['parcel_order'],
                config['truck_order'],
                stats['unused_trucks'],
                stats['unused_space'],
                stats['avg_distance'],
                stats['avg_fullness'],
                stats['unscheduled']))


def main(config_file):
    """Compare all algorithms on a single problem.

    Run the random algorithm and every configuration of the greedy
    algorithm on the scheduling problem defined in <config_file>.

    Precondition: <config_file> is a json file with keys and values
    as in the dictionary format defined in Assignment 1.

    @type config_file: str
    @rtype: None
    """
    with open(config_file, 'r') as file:
        basic_config = json.load(file)

    # We will use the keys 'parcel_file', 'fleet_file' and 'map_file' from
    # the dict <basic_config>.
    # If it has any other keys, we will ignore them.  Instead of taking the
    # algorithm configuration from a file, we try all possible configurations.

    # List of possible configurations for the scheduling algorithm.
    algorithm_configurations = [
        # --- Random
        {'algorithm': 'random',
         'parcel_priority': 'NA',
         'parcel_order': 'NA',
         'truck_order': 'NA'},
        # --- Greedy by volume, with 4 sub-configurations
        {'algorithm': 'greedy',
         'parcel_priority': 'volume',
         'parcel_order': 'non-decreasing',
         'truck_order': 'non-decreasing'},
        {'algorithm': 'greedy',
         'parcel_priority': 'volume',
         'parcel_order': 'non-decreasing',
         'truck_order': 'non-increasing'},
        {'algorithm': 'greedy',
         'parcel_priority': 'volume',
         'parcel_order': 'non-increasing',
         'truck_order': 'non-decreasing'},
        {'algorithm': 'greedy',
         'parcel_priority': 'volume',
         'parcel_order': 'non-increasing',
         'truck_order': 'non-increasing'},
        # --- Greedy by destination, with 4 sub-configurations
        {'algorithm': 'greedy',
         'parcel_priority': 'destination',
         'parcel_order': 'non-decreasing',
         'truck_order': 'non-decreasing'},
        {'algorithm': 'greedy',
         'parcel_priority': 'destination',
         'parcel_order': 'non-decreasing',
         'truck_order': 'non-increasing'},
        {'algorithm': 'greedy',
         'parcel_priority': 'destination',
         'parcel_order': 'non-increasing',
         'truck_order': 'non-decreasing'},
        {'algorithm': 'greedy',
         'parcel_priority': 'destination',
         'parcel_order': 'non-increasing',
         'truck_order': 'non-increasing'}
        ]

    with open('data/results.csv', 'w') as file:
        print_table_title(file)
        for item in algorithm_configurations:
            # Start with the basic configuration <config>, and add the
            # algorithm details from this item in our list of configurations.
            config = basic_config.copy()
            config.update(item)
            # Run an experiment on this configuration and print the results
            # to our csv file.
            expt = SchedulingExperiment(config)
            results = expt.run(report=False)
            print_table_row(config, results, file)

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='.pylintrc')
    main('data/demo.json')
