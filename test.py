from ConvexPolygon import ConvexPolygon
import numpy as np

def main():
    test = ConvexPolygon((0,0), 1)
    print(test.isConvex())
main()