import math as m
import matplotlib.pyplot as plt

class ConvexPolygon:
    def __init__(self, c : tuple, r : int):
        self.center_point = c
        self.radius = r
        self.x_points = [(self.center_point[0] + self.radius * m.cos(x)) for x in self.drange(0, 2 * m.pi, 0.05)]
        self.y_points = [(self.center_point[1] + self.radius * m.sin(y)) for y in self.drange(0, 2 * m.pi, 0.05)]

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
'''
    def isConvex(self):
        signs = [zCrossProduct(a, b, c) > 0 for a, b, c in zip(vertices[2:], vertices[1:], vertices)]
        return all(signs) or not any(signs)
    def crossProduct(self, a, b, c):
        return (a[0] - b[0]) * (b[1] - c[1]) - (a[1] - b[1]) * (b[0] - c[0])
'''