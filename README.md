# Numerical_Analysis
Quick and dirty programs I wrote in Python for a Numerical Analysis course

bisectionMethod.py is a program that finds a zero of a function on [lo,hi] (entered by the user)

fixedPointIteration.py is a program that uses fixed point iteration to find a root of a function

gaussianElimination.py is a program that row reduces a matrix to RREF

jacobiMethod.py is a program that uses Jacobi method (a form of fixed point iteration) to solve a system of equations

leastSquares.py is a program that uses the Least Squares method to solve an over-determined system of equations

LUDecompostion.py is a program that decomposes a matrix into one of its infinite LU forms, yielding a lower-triangular matrix L and an upper-triangular matrix U such that the original matrix A = LU

matrixOperations.py is a program that contains basic matrix operations like addition, multiplication, transpose, determinant and the like

newtonMethod.py is a program that uses Newton's Method to find the root of an equation. (Note: the derivative of a function f at x_0 has been approximated by (f(x)-f(x-10**-4))/10**-4, so this really is just the Secant Method. You could hardcode the derivative of your function in if you please)

polynomialInterpolator.py is a program that finds a polynomial of degree n-1 that interpolates the points (x1, y1), (x2, y2), ..., (x_n, y_n) by forming a system of equations and solving the system using Kramer's method

systemSolverKramer.py is a program that solves a system of equations using Kramer's method
