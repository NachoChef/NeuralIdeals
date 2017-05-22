from shapely import geometry as g
from matplotlib import pyplot as plt
from descartes import PolygonPatch
from shapely.geometry.polygon import LinearRing, Polygon

p1 = g.Point(0,0)
p2 = g.Point(1,0)
p3 = g.Point(1,1)
p4 = g.Point(0,1)

pointList = [p1, p2, p3, p4, p1]

poly = g.Polygon([[p.x, p.y] for p in pointList])
x,y = poly.exterior.xy
fig = plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)
ax.plot(x, y, color='#6699cc', alpha=0.7,
    linewidth=3, solid_capstyle='round', zorder=2)
ax.set_title('Polygon')
plt.show()