import math as m
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np

"""



A polygon generator, generating the points for a circle of specified radius at a specified center point.

These points may then be modified as desired and the shape may be adjusted while checking for convexity.

AUTHORS:

- Justin Jones (2017-06) [initial version]

"""


class ConvexPolygon:


    def __init__(self, c : tuple, r : int):
        r"""

            Constructs a simple, circular polygonal shape. Before modification, the shape is convex.

        INPUT:

        - ``c`` -- a 2-integer tuple indicating x, y values

        - ``r`` -- an integer indicating the radius of the shape

        OUTPUT:

            None

        EXAMPLE:

                >>> C = ConvexPolygon((0,0), 1)

        """
        self.center_point = c
        self.radius = r
        self.x_points = [(self.center_point[0] + self.radius * m.cos(x)) for x in self.drange(0, 2 * m.pi, 0.05)]
        self.y_points = [(self.center_point[1] + self.radius * m.sin(y)) for y in self.drange(0, 2 * m.pi, 0.05)]
        self.points = {(i+1) : (self.x_points[i], self.y_points[i]) for i in range(len(self.x_points))}

    def drange(self, start, stop, step):
        r"""

        A simple, fully inclusive generator allowing the use of non-integer steps.

        INPUT:

        - ``start`` -- The beginning range value

        - ``stop`` -- The ending range value

        - ``step`` -- The incremental step value to take for every iteration

        OUTPUT:

            A integer or double between start and stop.

        EXAMPLES:

            >>> for x in drange (0, 1, 0.2):
                    print(x, end = ' ')
            0, 0.2, 0.4, 0.6, 0.8, 1.0

        """
        tmp = start
        while tmp <= stop:
            yield tmp
            tmp += step

    def testPlot(self):
        r"""

        	Prints a plot of the parent object utilizing matplotlib.

        INPUT:

        	None

        OUTPUT:

        	A plot of the parent object points.

        EXAMPLE:

        	>>> circle = ConvexPolygon((0, 0), 1)
        	>>> circle.testPlot()

        """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.set_xlim(self.center_point[0] - self.radius, self.center_point[0] + self.radius)
        ax.set_ylim(self.center_point[1] - self.radius, self.center_point[1] + self.radius)
        ax.plot(self.x_points, self.y_points)
        ax.set_title('Test plot')
        plt.show()

    def toString(self):
        r"""

        	Will print the list of the points described in parent object.

        INPUT:

        	None

        OUTPUT:

        	2 rows of lists

        EXAMPLE:

        	>>> circle = ConvexPolygon((0, 0), 1)
        	>>> circle.toString()
        	X values: 1.0, 0.9987, 0.995, [...]
        	Y values: 0.0, 0.0499, 0.0998, [...]

        """
        print("X values: " + str(self.x_points))
        print("Y values: " + str(self.y_points))

    def isConvex (self):
        r"""
        
            Tests convexity by checking whether the current number of points is equal to the number of points calculated
            as the ConvexHull.
            
        INPUT:
            
            None
            
        OUTPUT:
        
            Boolean true if convex, false if not convex.
             
        EXAMPLE:
            
            >>> circle = ConvexPolygon((0,0), 1)
            >>> circle.isConvex()
            True
            
        """
        npa = np.asfarray(self.points.values())
        return len(self.points) == len(ConvexHull(npa).simplices)

    def modify(self, check=True, **kwargs):
        r"""
        
            Takes a variable-length set of point numbers and coordinates, performs the modifications,
            and checks convexity by default.
        
        :param points: 
        
        :param check:
         
        :return: None
        
        EXAMPLE:
        
            >>> circle = ConvexPolygon((0, 0), 1)
            >>> point_int = (1, 2, 3)
            >>> point_coord = ((0,0), (1,1), (2,2))
            >>> circle.modify(False, point_int, point_coord)
        
        """
        try:
            temp = self.points
            for point, coord in kwargs.items():
                self.points[point] = coord
            if check:
                if not self.isConvex():
                    raise ValueError('The supplied point resulted in a non-convex shape.')
        except ValueError as err:
            self.points = temp
            print(err.args)