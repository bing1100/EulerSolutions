#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?

# This is a standard path problem. If we name each lattice point a particular name
#  and we calculate the number of paths that you can use to get to the lattice point
#  we can use recursion to get from one end to the other end. 

# We can simply use the binomial thereom as this is a special application of pascals
# triangle

# We are calculating nCr where n is 2*(j-1) (in a j by j lattice square) and r is j -1

import math

def f_f(j):
    n=2*j
    r=n//2
    num=math.factorial(n)
    den=math.factorial(n-r) * math.factorial(r)
    return num//den
    