import sympy as sp

print("====================================================")
print("               Derivative Calculator                ")
print("====================================================")
print(" ")

x = sp.Symbol('x')

a = input("Equation: ")

print("First Derivative: ", sp.diff(a, x, 1))
print("Second Derivative: ", sp.diff(a, x, 2))
print("Thrid Derivative: ", sp.diff(a, x, 3))
