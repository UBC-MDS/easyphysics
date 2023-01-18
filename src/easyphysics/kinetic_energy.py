def kinetic_energy(m, v):
    """Calculates the Kinetic Energy of an object. When work is done on an object, energy is transferred, and the object moves with a new constant speed. We call the energy that is transferred kinetic energy, and it depends on the mass and speed achieved. 
    The kinetic energy equation is given as:
    KE = 1/2*m*v^2
    Where KE is the kinetic energy, m is the body’s mass, and v is the body’s velocity.

    Parameters
    ---------------
    m : numeric
        mass of the object (kg)
    v: numeric
       velocity of the object (m/s)

    return
    ---------------
    KE: numeric
        kinetic energy of the object

    Examples
    ---------------
    >>> kinetic_energy(0.6, 3)
    2.7
    """
    KE = m*v*v/2
    return KE
