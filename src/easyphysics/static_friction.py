
def static_friction_ground(mu, m, g = 9.8):
    """ calculating the friction force for static object. The formula is fr = mu * N, where 
    the mu is the coefficient of friction which incorporating the characteristics of the surface.
    For example, if you want to calculate the friction when you put your phone on a table, then the coefficient of friction is 
    depending on the matirial of the table. N is the normal force which means the perpendicular force of the surface which object 
    touching on. In our case, it would be m*g since it is on the ground. fr = mu * m * g. 
    
    Parameters
    ---------------
    mu : numeric 
        coefficient of friction
    m: numeric
        mass (kg)
    g: numeric, optimal     
        gravity on Earth
    
    return
    ---------------
    force: numeric
        static friction force
        
    Examples
    ---------------
    >>> static_friction_ground(0.2, 2)
    3.92
    >>> static_traction_ground(0.2, 2, g = 10)
    4
    """
    result = 0
    return result
