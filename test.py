from ConvexPolygon import ConvexPolygon
import numpy as np
from InductiveCirclesInclusion import sort

def main():
    codes = [[1,0,0], [0,1,0],[0,0,1], [1,1,0]]
    c2 = sort(codes)
    print(c2)
    print(sort(c2[0:2], 1) + sort(c2[2:], 1))
main()