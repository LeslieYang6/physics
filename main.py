# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sympy as sp

a_N=sp.symbols("a_N")
a_M=sp.symbols("a_M")
a_0=sp.symbols("a_0")
eq=sp.Eq(a_N,a_M*(a_M/a_0)/(sp.sqrt(1+(a_M/a_0)**2)))

print(sp.solve(eq,a_M))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
