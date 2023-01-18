import sys
#sys.path.append("..\\src\\")
print(sys.path)
from easyphysics.kinetic_energy import kinetic_energy 

def test_kinetic_energy():
    m = 10
    v = 2.3
    expected = 26.45
    actual = kinetic_energy(m, v)
    assert actual == expected, "Kinetic Energy is wrong! Check again!"
