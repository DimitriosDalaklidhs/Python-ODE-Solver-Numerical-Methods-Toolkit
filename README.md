ODE Numerical Solver & Method Comparison

A Python project implementing and comparing multiple numerical methods for solving ODEs.

🌟 Overview

This project implements and compares three numerical integration methods for solving first-order Ordinary Differential Equations (ODEs):

Forward Euler

Central Difference (two-step method)

Improved Euler (Heun’s method)

It evaluates each method’s accuracy against a known analytical solution, computes max errors, prints detailed step-by-step tables, and generates Matplotlib visualizations.

The project was developed using PyCharm, with a clean modular structure and emphasis on clarity, numerical correctness, and error analysis.

 Features
✔ Numerical Methods Implemented

Forward Euler

Central Difference (startup via Euler)

Improved Euler (Heun)

✔ Accuracy & Error Analysis

Exact solution y_exact(t) for benchmarking

Error tables for each numerical method

Maximum absolute error per run

Side-by-side comparison plots

✔ Visualization

Matplotlib graphs showing numerical curves vs exact solution

Clean comparison between solvers

Adjustable step size h for convergence experiments

✔ Modular Structure

main.py — numerical methods, execution logic, plotting

ext_func.py — ODE definition and analytical solution

 Project Structure
PYTHON_ODE/
│
├── main.py         # Numerical methods and plotting
├── ext_func.py     # ODE function f(t,y) and analytical solution
└── README.md

 Mathematical Background

We solve initial value problems (IVPs) of the form:

𝑦
′
(
𝑡
)
=
𝑓
(
𝑡
,
𝑦
)
,
𝑦
(
𝑎
)
=
𝑦
0
y
′
(t)=f(t,y),y(a)=y
0
	​


For the project, two example problems are provided (selectable in ext_func.py):

Problem 1
𝑦
′
=
2
𝑦
,
𝑦
(
𝑡
)
=
𝑒
2
𝑡
y
′
=2y,y(t)=e
2t
Problem 2
𝑦
′
(
𝑡
)
=
1
−
2
𝜋
sin
⁡
(
2
𝜋
𝑡
)
,
𝑦
(
𝑡
)
=
𝑡
+
cos
⁡
(
2
𝜋
𝑡
)
y
′
(t)=1−2πsin(2πt),y(t)=t+cos(2πt)
 Usage
▶ Run the program:
python main.py

The script will ask:

a: start of interval

b: end of interval

y0: initial condition

Whether to automatically run with h = 0.2 and h = 0.1

Example:

Δώσε δεδομένα αρχικού προβλήματος y'(t)=f(t,y), y(a)=y0
a: 0
b: 1
y0: 1
Θες να τρέξω για h=0.2 και h=0.1; [y/n]:


Plots will automatically appear showing each method vs the exact solution.



(Values depend on the chosen ODE and step size.)

Technologies Used

Python 3

NumPy — numerical computation

Matplotlib — plotting & visualization

PyCharm — development environment

 License

This project is MIT licensed.

 Author

Dimitrios Dalaklidis
Junior Backend / Systems / Python Developer
GitHub Profile
