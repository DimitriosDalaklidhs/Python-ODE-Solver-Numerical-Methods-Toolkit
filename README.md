This project compares three numerical integration methods (Euler, Improved Euler) implemented in Python this time. Demonstrates algorithmic reasoning.

Implements numerical methods for solving first-order Ordinary Differential Equations (ODEs) of the form:

y'(t) = f(t, y), y(a) = y₀

It provides three common numerical solvers:

FE (Forward Euler)
CD (Central Difference / Modified Euler)
IE (Improved Euler)
Example:

Enter initial value problem data y'(t)=f(t,y), y(a)=y0 a: 0 b: 1 y0: 1 Do you want to run for h=0.2 and h=0.1? [y/n]: y

Example output:

Max error FE: 2.010816e+000 Max error CD: 6.156161e-001 Max error IE: 2.882349e-001


Mathematical Model
For PROBLEM_ID = 1,
f(t, y) = 2y → exact solution y(t) = e^(2t)
For PROBLEM_ID = 2,
f(t, y) = 1 − 2πsin(2πt) → exact solution y(t) = t + cos(2πt)



**PROJECT STRUCTURE**
PYTHON_ODE/
│
├── main.py          # Numerical methods, execution logic, error tables, plots
├── ext_func.py      # External definition of f(t,y) and the exact solution
└── README.md

**Conclusions (General)**

The Improved Euler (Heun) method provides significantly better accuracy for the same step size.

The Central Difference method is more accurate than Forward Euler but depends on the startup value.

As the step size h decreases, errors decrease for all methods (expected convergence behavior).

Visualization clearly shows the superiority of Improved Euler, especially for Problem 2.

**Technologies Used**

Python 3

NumPy

Matplotlib

PyCharm (development environment)
**AUTHOR**
Dimitrios Dalaklidhs, Backend Developer
