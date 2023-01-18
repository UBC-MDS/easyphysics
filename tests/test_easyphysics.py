import sys
#sys.path.append("..\\src\\")
print(sys.path)
from easyphysics.kinetic_energy import kinetic_energy
from easyphysics.gravitational_energy import gravitational_energy
from easyphysics.freefall import freefall
import matplotlib
import pytest

def test_kinetic_energy():
    m = 10
    v = 2.3
    expected = 26.45
    actual = kinetic_energy(m, v)
    assert actual == expected, "Kinetic Energy is wrong! Check again!"
    
def test_freefall():
    """ Test freefall function time and plot"""
    expected_time1 = 1.4286
    actual_time1, plot1 = freefall(10)
    expected_time2 = 14.142
    actual_time2, plot2 = freefall(100, g = 10)
    expected_time3 = 0.3162
    actual_time3, plot3 = freefall(5, g = 100)    
    assert round(expected_time1,2) == round(actual_time1,2)
    assert round(expected_time2,2) == round(actual_time2,2)
    assert round(expected_time3,2) == round(actual_time3,2)
    assert type(plot1) == matplotlib.figure.Figure, \
           "Not a plot returned!"
    assert type(plot2) == matplotlib.figure.Figure, \
           "Not a plot returned!"
    assert type(plot3) == matplotlib.figure.Figure, \
           "Not a plot returned!"

def test_gravitation_energy():
    """ Test Gravitational Energy"""
    expected1 = 245.16
    expected2=2157.463 
    actual1 = gravitation_energy(2.5, g = 9.8,10)
    actual2 = gravitational_energy(10, g = 9.80665, 22)
    
    assert round(actual1,2) == round(expected1,2), "Gravitation Energy calculated is not right! Do Check inputs"
    assert round(actual2,2) == round(expected2,2), "Gravitation Energy calculated is not right! Do Check inputs"