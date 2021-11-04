"""
Name: Dojae Kim
Student Number: 400420323
Student email: kim408@mcmaster.ca
File name: Assignment 5 test traffic light file.
"""

from A5.stubs_traffic_light import Intersection
import time


# initial lights test.
# when the main road signal is green the side road must always be red.
# testing for condition a)
def test_initial_signals_part_a():
    intersection = Intersection()

    assert intersection.mainRoadCar != intersection.sideRoadCar, "Error! Test for condition a) failed!"


# initial lights test.
# when the main road signal is green the pedestrian signal must be green
# testing for condition b)
def test_initial_signals_part_b():
    intersection = Intersection()

    assert intersection.mainRoadCar == intersection.mainRoadPedestrian and intersection.sideRoadCar == intersection.sideRoadPedestrian, "Error! Test for condition b) failed!"


# testing lights again AFTER lights change
# testing for condition a)
def test_change_signals_part_a():
    intersection = Intersection()
    intersection.changeSignals()

    assert intersection.mainRoadCar != intersection.sideRoadCar and intersection.mainRoadPedestrian != intersection.sideRoadPedestrian, "Error! Test for condition a) failed!"


# testing lights again AFTER lights change
# testing for condition b)
def test_change_signals_part_b():
    intersection = Intersection()
    intersection.changeSignals()

    assert intersection.mainRoadCar == intersection.mainRoadPedestrian and intersection.sideRoadCar == intersection.sideRoadPedestrian, "Error! Test for condition b) failed!"


# first, the main roads are GREEN and side roads are RED
# traffic on the side street has been waiting for more than 100 seconds,
# so lights should have changed at this point in time
# now, we expect main roads to be RED and side roads to be GREEN
def test_timing_for_part_c():
    intersection = Intersection()
    intersection.simulate_first_signals_change()
    time.sleep(100)
    # after the first signals change (any time 90 seconds after simulate_first_signals_change() has
    # been called, the main road lights should have changed to RED and the side road lights should have changed
    # to GREEN. Hence, it would also be valid to test any other time greater than 90 here.
    assert intersection.mainRoadCar == "RED" and intersection.mainRoadPedestrian == "RED" and intersection.sideRoadCar == "GREEN" and intersection.sideRoadPedestrian == "GREEN", "Error! Test for condition c) failed!"
