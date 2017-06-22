from ConvexPolygon import ConvexPolygon
import numpy as np
from InductiveCirclesInclusion import *
from pc_tree import pc_tree

def main():

    codes = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
    test = pc_tree(codes, 3, 3)
    print(test)
main()