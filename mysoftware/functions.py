import numpy as np

def square(x):
    '''
    Takes a number x and squares it.

    Parameters:
    -----------
    x, float or int:
        Number which is to be squared.

    Returns:
    --------
    float:
        Square of x

    Examples:
    ---------

    >>> square(2)
    4

    >>> square(5)
    25

    >>> square(-1)
    1
    '''
    return x*x

def oneoverr(x):
    return 1/x


def CentralDifference(f,x,h):
    return((f(x+h) - f(x-h)) / (2*h))


for i in range(2, 8):
    h = 10**(-i)
    print(h, abs(CentralDifference(np.sin, 0.0, h) -1.0))
