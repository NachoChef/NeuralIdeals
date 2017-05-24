import math as m
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib import pyplot

class ConvexPolygon:
    def __init__(self, c : tuple, r : int):
        self.center_point = c
        self.radius = r
        self.x_points = [(self.center_point[0] + self.radius * m.cos(x)) for x in self.drange(0, 2 * m.pi, 0.1)]
        self.y_points = [(self.center_point[1] + self.radius * m.sin(y)) for y in self.drange(0, 2 * m.pi, 0.1)]

    def drange(self, start, stop, step):
        tmp = start
        while tmp < stop:
            yield tmp
            tmp += step

    def testPlot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim(self.center_point[0] - self.radius, self.center_point[0] + self.radius)
        ax.set_ylim(self.center_point[1] - self.radius, self.center_point[1] + self.radius)
        ax.plot(self.x_points, self.y_points)
        ax.set_title('Test plot')
        plt.show()

    def showPoints(self):
        print(self.x_points)
        print(self.y_points)
