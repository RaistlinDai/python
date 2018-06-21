'''
Created on Jun 20, 2018

This is a functional class for studying

@author: ftd
'''
import math

# abs math
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('incorrect operand type')
    if x >= 0:
        return x
    else:
        return -x

# New position
def my_move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# Power math
def my_power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# n! = 1 x 2 x 3 x ... x n
def my_fact(n):
    if n==1:
        return 1
    return n * my_fact(n - 1)

# The input order 01
# name, age are mandatory parameter
# nation is default parameter
# city is dynamic parameter (list)
def my_keyword01(name, age, nation='China', *city, **comments):
    print(name, age, nation, city, comments)
# The input order 02
def my_keyword02(name, age, nation='China', *, city, **comments):
    print(name, age, nation, city, comments)

# The third number is the sum of the first and the second
def my_Fibonacci(*, fir, maxC):
    n, a = 0, 0
    while n < maxC:
        yield fir
        a, fir = fir, fir + a
        n = n + 1
    print('done')

    