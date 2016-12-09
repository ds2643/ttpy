# an example program used for tests to represent valid python syntax
import sys
import random as r

# some comment

def foo(a, b, c):
    ''' example function '''
    return a + b + c

SOME_LIST = [x**2 for x in range(15)]

def bar():
    ''' another example function '''
    return [x for x in range(10)]

SOME_GLOBAL_VALUE = 5

def baz(a):
    ''' yet another example function '''
    assert(isinstance(a,int))
    return a ** 2

if __name__ == "__main__":
    print("this is a sample file")
    baz(5)
