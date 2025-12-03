 Objective

This project implements numerical methods for the approximate solution of the Initial Value Problem:

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
(
𝑡
)
)
,
𝑡
∈
[
𝑎
,
𝑏
]
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
(t)=f(t,y(t)),t∈[a,b],y(a)=y
0
	​


The following numerical methods are applied:

Forward Euler Method (FE / FD)

Central Difference Method (CD)

Improved Euler Method (Heun’s Method, IE)

The implementation is done in Python, following the assignment requirements:

The function 
𝑓
(
𝑡
,
𝑦
)
f(t,y) is implemented in a separate external file

Inputs 
𝑎
,
𝑏
,
𝑦
0
,
ℎ
a,b,y
0
	​

,h are provided dynamically during execution

The code prints numerical tables, error calculations, and generates graphical comparisons

 Project Structure
PYTHON_ODE/
│
├── main.py          # Numerical methods, execution logic, error tables, plots
├── ext_func.py      # External definition of f(t,y) and the exact solution
└── README.md

 Partition of the Interval Δ(J)

The interval 
[
𝑎
,
𝑏
]
[a,b] is divided into 
𝑁
N uniform steps using:

𝑡
𝑛
+
1
=
𝑡
𝑛
+
ℎ
t
n+1
	​

=t
n
	​

+h

where

𝑁
=
𝑏
−
𝑎
ℎ
N=
h
b−a
	​


A consistent time grid is used for all numerical methods, and its correctness is ensured using assert statements.

🔢 Numerical Methods Implemented
1️⃣ Forward Euler (FD)

Discrete analogue:

𝑦
𝑛
+
1
=
𝑦
𝑛
+
ℎ
 
𝑓
(
𝑡
𝑛
,
𝑦
𝑛
)
y
n+1
	​

=y
n
	​

+hf(t
n
	​

,y
n
	​

)
2️⃣ Central Difference (CD)

Startup (using Forward Euler):

𝑦
1
=
𝑦
0
+
ℎ
 
𝑓
(
𝑡
0
,
𝑦
0
)
y
1
	​

=y
0
	​

+hf(t
0
	​

,y
0
	​

)

Main recursion:

𝑦
𝑛
+
1
=
𝑦
𝑛
−
1
+
2
ℎ
 
𝑓
(
𝑡
𝑛
,
𝑦
𝑛
)
y
n+1
	​

=y
n−1
	​

+2hf(t
n
	​

,y
n
	​

)
3️⃣ Improved Euler (Heun Method, IE)
𝑘
1
=
𝑓
(
𝑡
𝑛
,
𝑦
𝑛
)
k
1
	​

=f(t
n
	​

,y
n
	​

)
𝑘
2
=
𝑓
(
𝑡
𝑛
+
ℎ
,
  
𝑦
𝑛
+
ℎ
𝑘
1
)
k
2
	​

=f(t
n
	​

+h,y
n
	​

+hk
1
	​

)
𝑦
𝑛
+
1
=
𝑦
𝑛
+
ℎ
2
(
𝑘
1
+
𝑘
2
)
y
n+1
	​

=y
n
	​

+
2
h
	​

(k
1
	​

+k
2
	​

)
 Problems Considered
Problem 1

𝑎
=
0
,
  
𝑏
=
1
,
  
𝑦
0
=
1
a=0,b=1,y
0
	​

=1

𝑓
(
𝑡
,
𝑦
)
=
2
𝑦
f(t,y)=2y

Exact solution:

𝑦
(
𝑡
)
=
𝑒
2
𝑡
y(t)=e
2t
Problem 2

𝑎
=
0
,
  
𝑏
=
𝜋
2
,
  
𝑦
0
=
1
a=0,b=
2
π
	​

,y
0
	​

=1

𝑓
(
𝑡
,
𝑦
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
f(t,y)=1−2πsin(2πt)

Exact solution:

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
y(t)=t+cos(2πt)
 Step Sizes Used

According to the assignment requirements, computations are performed for:

ℎ
=
0.2
h=0.2

ℎ
=
0.1
h=0.1

The program prints detailed solution tables for each method and computes the maximum error:

𝑒
𝑖
=
max
⁡
𝑖
∣
𝑦
(
𝑡
𝑖
)
−
𝑦
𝑖
∣
e
i
	​

=
i
max
	​

∣y(t
i
	​

)−y
i
	​

∣
 Error Comparison Table (Example Format)
Method	Max Error (h = 0.2)	Max Error (h = 0.1)
Forward Euler	…	…
Central Difference	…	…
Improved Euler	…	…

(Exact values depend on the chosen problem and step size.)

 Graphical Output

For each problem, and especially for 
ℎ
=
0.1
h=0.1, the program generates plots with:

Exact solution

Numerical solutions (FD, CD, IE)

All curves appear in the same graph to easily observe differences in accuracy and stability.

💬 Conclusions (General)

The Improved Euler (Heun) method provides significantly better accuracy for the same step size.

The Central Difference method is more accurate than Forward Euler but depends on the startup value.

As the step size h decreases, errors decrease for all methods (expected convergence behavior).

Visualization clearly shows the superiority of Improved Euler, especially for Problem 2.

 Technologies Used

Python 3

NumPy

Matplotlib

PyCharm (development environment)

 Author

Dimitrios Dalaklidis
 Backend & Systems Developer
GitHub: DimitriosDalaklidhs
