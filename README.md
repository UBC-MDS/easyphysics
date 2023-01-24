# easyphysics

A package with useful physics formulas to make physics easy and fun for users! It uses four functions to easily calculate four classic physics theories. By making the functions concise and supporting graphs to demonstrate the theories, physics beginners might find learning physics fun and not daunting! All functions in this package require only arguments in numeric format; no dataset files are needed. `easyphysics` can also generate easy-to-understand visualizations to further reveal the physics effects.  

## Installation

```bash
$ pip install easyphysics
```

## Usage

The package has four functions which can provide solutions for Physics Equations. Input will be taken from the User and the solutions will be provided by the functions. The four functions are as follows: 


- `freefall()` calculates the time it takes for a falling object using the equation of motion height = 1/2*gt^2, given the height and gravity of the free fall. It returns the time it takes for the free fall, and a plot compares the time of the free fall on different planets with a list. The distance traveled by the falling object (height) and the acceleration of gravity (g, default = 9.8) are the function’s arguments. 
- `gravitational_energy()` calculates the energy possessed or acquired by an object due to a change in its position when it is present in a gravitational field  = m*g*h
- `kinetic_energy()` calculates the Kinetic Energy of an object. When work is done on an object, energy is transferred, and the object moves with a new constant speed. We call the energy that is transferred kinetic energy, and it depends on the mass and speed achieved. The kinetic energy equation is given as: KE = 1/2*m*v^2, Where KE is the kinetic energy, m is the body’s mass, and v is the body’s velocity.
- `static_friction_ground()` calculates the friction force for static object. The formula is fr = mu * N, where 
    the mu is the coefficient of friction which incorporating the characteristics of the surface.

```python
from easyphysics.freefall import freefall
import matplotlib.pylab as plt
time, plot = freefall(height, g = 9.8)

```
## Fitting into the Python ecosystem

A similar well-known package [sympy](https://github.com/sympy/sympy) is available, which has a [module in physics](https://docs.sympy.org/latest/reference/public/physics/index.html).`sympy` is a library for symbolic computation. The physics module focuses on solving advanced physics problems such as Hydrogen Wavefunction and Quantum physics.

`easyphysics` targets physics beginners rather than professionals, such as middle schoolers and people new to physics. It uses four functions to easily calculate four classic physics theories. By making the functions concise and supporting graphs to demonstrate the theories, physics beginners might find learning physics fun and not daunting! All functions in this package require only arguments in numeric format; no dataset files are needed.  `easyphysics` can also generate easy-to-understand visualizations to further reveal the physics effects.  The specific functions and visual components make  `easyphysics` different from other packages.

## Contributing

`easyphysics` was created by Revathy Ponnambalam, Nikita Susan Easow, Yaou Hu and Mengjun Chen.
Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`easyphysics` was created by Revathy Ponnambalam, Nikita Susan Easow, Yaou Hu and Mengjun Chen. It is licensed under the terms of the MIT license.

## Credits

`easyphysics` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
