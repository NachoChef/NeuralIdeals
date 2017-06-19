from ConvexPolygon import ConvexPolygon
import numpy as np
from InductiveCirclesInclusion import *

def main():
    codes = [[1, 0, 0], [1, 0, 1], [0, 1, 1]]
    c = sort(codes)
    print(c)
    print(is_oscillating(c))
main()