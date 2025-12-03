# f_function.py
import numpy as np

#  ΠΡΟΒΛΗΜΑ: 1 ή 2
PROBLEM_ID = 2
# PROBLEM_ID = 2

def f(t, y):

    if PROBLEM_ID == 1:
        return 2.0 * y
    elif PROBLEM_ID == 2:
        return 1.0 - 2.0 * np.pi * np.sin(2.0 * np.pi * t)
    else:
        raise ValueError("PROBLEM_ID must be 1 or 2")

def y_exact(t):
    """
    Ακριβής λύση, για έλεγχο/σφάλματα/γραφήματα.
    Πρόβλημα 1: y(t) = e^{2t}
    Πρόβλημα 2: y(t) = t + cos(2π t)
    """
    if PROBLEM_ID == 1:
        return np.exp(2.0 * t)
    elif PROBLEM_ID == 2:
        return t + np.cos(2.0 * np.pi * t)
    else:
        raise ValueError("PROBLEM_ID must be 1 or 2")
