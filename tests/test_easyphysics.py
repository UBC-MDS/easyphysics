import sys
#sys.path.append("..\\src\\")
print(sys.path)
from easyphysics.kinetic_energy import kinetic_energy
from easyphysics.gravitational_energy import gravitational_energy
from easyphysics.freefall import freefall
from easyphysics.static_friction import static_friction_ground
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
    
    # test three different input combinations
    expected_time1 = 1.4286
    actual_time1, plot1 = freefall(10)
    expected_time2 = 4.47
    actual_time2, plot2 = freefall(100, g = 10)
    expected_time3 = 0.3162
    actual_time3, plot3 = freefall(5, g = 100)    
    assert round(expected_time1,2) == round(actual_time1,2), "freefall calculation not correct"
    assert round(expected_time2,2) == round(actual_time2,2), "freefall calculation not correct"
    assert round(expected_time3,2) == round(actual_time3,2), "freefall calculation not correct"
    
    # test the output has a plot
    assert type(plot1) == matplotlib.figure.Figure, \
           "Not a plot returned!"
    assert type(plot2) == matplotlib.figure.Figure, \
           "Not a plot returned!"
    assert type(plot3) == matplotlib.figure.Figure, \
           "Not a plot returned!"
    
    # test inputting height as not a number
    with pytest.raises(TypeError):
        freefall('a')
    
    # test input g as not a number
    with pytest.raises(TypeError):
        freefall(100, g = 'g')
        
def test_gravitation_energy():
    """ Test Gravitational Energy"""
    expected1 = 245.00
    expected2 = 2157.463 
    actual1 = gravitational_energy(2.5,10,g = 9.8)
    actual2 = gravitational_energy(10,22,g = 9.80665)
    
    assert round(actual1,2) == round(expected1,2), "Gravitation Energy calculated is not right! Do Check inputs"
    assert round(actual2,2) == round(expected2,2), "Gravitation Energy calculated is not right! Do Check inputs"
    

    
def test_friction():
    """ Test Friction Force on Ground """
    expected1 = 3.92
    expected2 = 6.6
    actual1 = static_friction_ground(mu=0.2, m=2, g=9.8)
    actual2 = static_friction_ground(mu=0.3, g = 10, m=2.2)
    
    assert round(actual1,2) == round(expected1,2), "Friction force calculated is not right! Do Check inputs"
    assert round(actual2,2) == round(expected2,2), "Friction force calculated is not right! Do Check inputs"
