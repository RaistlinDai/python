'''
Created on Jun 20, 2018

This is a functional class for studying

@author: ftd
'''
import math

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


def my_power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s