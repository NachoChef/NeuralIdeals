from ConvexPolygon import ConvexPolygon
import numpy as np
from InductiveCirclesInclusion import sort

def main():
    codes = [[1,1,0], [1,0,0], [1,0,1]]
    print(sort(codes))
main()