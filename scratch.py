import networkx as nx
import matplotlib.pyplot as plt
import re

# {x1x4, x1x5, x3x4, x3x5, x3(1 − x1), x5(1 − x2), x5(1 − x4)}
l = str('[x1*x4, x1*x5, x3*x4, x3*x5, x3*(1 − x1), x5*(1 − x2), x5*(1 − x4)]')
s = l.split(',')

res = (tuple(map(int, re.findall(r'x(\d+)', x))) for x in s)
res = set((tuple(sorted(i)) for i in res))
length = 5
#adjusted for 1 based
total = sum(([sorted((i,j)) for j in range(1,length+1) if j is not i] for i in range(1,length+1)),[])
total = set(tuple(i) for i in total)
print(res)
print(total)
print(total - res)

G = nx.Graph()
G.add_node(5)
G.add_edges_from(list(total - res))
nx.draw(G, with_labels=True)
plt.show()
'''
type1 = x(\d+)\*x(\d+))(?:\*x(\d+))
type2 = x(\d+)\*\(
type3 = \(x(\d+)
'''