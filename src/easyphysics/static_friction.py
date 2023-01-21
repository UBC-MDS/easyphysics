import altair as alt
import numpy as np
import pandas as pd


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
    #checking the input values to be the right 
    if (type(mu) == int or type(mu) == float) & (type(g) == int or type(g) == float) & (type(m) == int or type(m) == float):                             :
        result = mu * m * g
    else:
        raise Exception('height and g has to be numeric!')

    return result

def plot_frict(m, mu, g):
    """
    Ploting the trend line for firction force in different masses 
    
    parameter
    ------------
    mu : numeric 
        coefficient of friction
    m: numeric
        mass (kg)
    g: numeric, optimal     
        gravity on Earth
    
    return
    ---------------
    plot
        
    Examples
    ---------------
    >>> static_friction_ground(0.2, 2)
    line plot 
    >>> static_traction_ground(0.2, 2, g = 10)
    line plot
    """
    
    if (type(mu) == int or type(mu) == float) & (type(g) == int or type(g) == float) & (type(m) == int or type(m) == float):
        
        masses = np.arange(0, m, 0.1)

        friction_line = [static_friction_ground(mu, i , g) for i in masses]

        source = pd.DataFrame({
            'mass': masses,
            'friction': friction_line
            })
        line = alt.Chart(source).mark_line().encode(
            x='mass',
            y='friction',
            tooltip = ['mass', 'friction']
        ).properties(
        title = "The static friction as mass increase"
        )
    else:
        raise Exception('height and g has to be numeric!')
        
    return line
