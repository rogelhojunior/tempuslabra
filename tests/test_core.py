from freezegun import freeze_time
from tempuslabra import timeit

from io import StringIO
import sys
import unittest


def dummy_function():
    return "Dummy Return"

def validate_output(expected_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            capturedOutput = StringIO()
            sys.stdout = capturedOutput
            result = func(*args, **kwargs)
            sys.stdout = sys.__stdout__  

            assert expected_output in capturedOutput.getvalue()

            return result
        return wrapper
    return decorator

class TestTimeIt(unittest.TestCase):

    @freeze_time("Dec 14th, 2023", auto_tick_seconds=15)
    @validate_output(expected_output='took 15 seconds to run.')
    @timeit
    def test_elapsed_seconds(self):
        dummy_function()

    @freeze_time("Dec 14th, 2023", auto_tick_seconds=65)
    @validate_output(expected_output='took 1 minutes and 5 seconds to run.')
    @timeit
    def test_elapsed_minute(self):
        dummy_function()

    @freeze_time("Dec 14th, 2023", auto_tick_seconds=155)
    @validate_output(expected_output='took 2 minutes and 35 seconds to run.')
    @timeit
    def test_elapsed_minutes(self):
        dummy_function()

    @freeze_time("Dec 14th, 2023", auto_tick_seconds=3715)
    @validate_output(expected_output='took 1 hours, 1 minutes and 55 seconds to run.')
    @timeit
    def test_elapsed_hour(self):
        dummy_function()

    @freeze_time("Dec 14th, 2023", auto_tick_seconds=9645)
    @validate_output(expected_output='took 2 hours, 40 minutes and 45 seconds to run.')
    @timeit
    def test_elapsed_hours(self):
        dummy_function()
