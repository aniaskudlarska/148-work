"""Assignment 1 - Tests

This module contains a test case that you can use once you have the entire
program completed, that is, after Task 6.

You would be wise to add further test cases and improve your confidence in
your code.

As you work through the earlier phases of the assignment, you can use doctest
and unittest to create and run tests of individual methods in your code.
"""

import unittest
from experiment import SchedulingExperiment


# -----------------------------------------------------------------------------
# Don't change this code!
# Unlike other sets of unit tests, rather than defining them explicitly, we're
# using helpers to generate them automatically.
# Skip down to the bottom of the file to see how you can add new tests.
# -----------------------------------------------------------------------------
class TestExperiment(unittest.TestCase):
    pass


def check_stat(config, stat, val):
    def test(self):
        experiment = SchedulingExperiment(config)
        results = experiment.run()
        self.assertEqual(round(results[stat], 1), round(val, 1))
    return test


def make_test(id, config, expected_stats):
    """Helper for making tests.

    Since all of the tests have the same format, it's useful to use this
    helper function instead of repeating lots of code.
    """
    root = 'test_' + id
    for key, value in expected_stats.items():
        setattr(TestExperiment,
                root + '__' + key,
                check_stat(config, key, value))


# -----------------------------------------------------------------------------
# Add your tests here!
# All tests will be in the form
# make_test(<test-name>, <config_dict>, <expected_stats_dict>)
#
# NOTE: if you get a "FileNotFoundError", try replacing the filename
# with the full path to the file (e.g., "C:\\Users\\David\\Documents\\...")
# -----------------------------------------------------------------------------

# Sample test
make_test('1-small',
          {
            'depot_location': 'Toronto',
            'parcel_file': 'data/parcel-data-small.txt',
            'truck_file': 'data/truck-data-small.txt',
            'map_file': 'data/map-data-2.txt',
            'algorithm': 'greedy',
            'parcel_priority': 'volume',
            'parcel_order': 'non-decreasing',
            'truck_order': 'non-decreasing',
            'verbose': 'false'},
          {
              'fleet': 3,
              'unused_trucks': 0,
              'unused_space': 0,
              'avg_distance': 96.3,
              'avg_fullness': 100,
              'unscheduled': 0
          })


if __name__ == '__main__':
    unittest.main()
