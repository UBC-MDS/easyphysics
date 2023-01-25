import numpy as np
import matplotlib.pylab as plt


def freefall(height, g=9.8):
    """ calculates the time it takes for a falling object
    using the equation of motion height = 1/2*gt^2, 
    given the height and gravity of the free fall. 
    It returns the time it takes for the free fall, 
    and a plot compares the time of the free fall 
    on different planets with a list. 
    The distance traveled by the falling object (height)
    and the acceleration of gravity (g, default = 9.8) 
    are the function’s arguments.
    
    Parameters
    ----------
    height : numeric
        A numeric value that is the distance of the free fall in meters.
    g: numeric, optional
       The gravity of the free fall (m/s^2), default value = 9.8.
    Returns
    -------
    time: float
        A float that is the time it takes for the free fall in seconds.
    plot: matplotlib.figure.Figure,
        A matplotlib.figure.Figure that compares time of a free fall with
        the height indicated by user on different planets.
    Examples
    --------
    >>> free_fall(10, g=9.8)
    1.4286
    >>> free_fall(10, g=274)
    0.2702
    """
    if (type(height) == int or type(height) == float) & (type(g) == int or type(g) == float):
        time = np.sqrt(2*height/g)
        gdict = {'Moon': 0.17,
                 'Mars': 0.38,
                'Uranus': 0.89,
                'Venus': 0.90,
                'Saturn': 1.07,
                'Sun': 27.9}
        gdict['Your planet'] = g/9.8
        sorted_gdict = dict(sorted(gdict.items(), key=lambda x:x[1]))
        planet = []
        gravity = []
        times = []
        for value in sorted_gdict.values():
            gravity.append(value)
        for key in sorted_gdict.keys():
            planet.append(key)
        for value in sorted_gdict.values():
            times.append(np.sqrt(2*height/(9.8*value)))
        plt.scatter(planet,times)
        plt.ylabel("Time for the free fall in seconds")
        plt.xlabel("Planets")
        plt.title("Time for the free fall on different planets for the height you entered")
        plt.figure(figsize = (10,10))
        plot = plt.figure()
    else:
        raise TypeError('height and g has to be numeric!')
    return time, plot
