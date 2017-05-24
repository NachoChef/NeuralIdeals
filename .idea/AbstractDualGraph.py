class AbstractDualGraph:

    def __init__(self, abrs : list):
        self.nodes = list()
        self.edges = list()
        for abr in abrs:
            nodes += AbstractDualNode(abr)
        for n in nodes:
            found_node_again = False
            for n2 in nodes:
                if not found_node_again:
                    if n2 == n:
                        found_node_again = False
                else:
                    straddlingCurve = n.abbr.getStraddledContour(n2.abr)
                    if straddlingCurve is not None:
                        add_edge (n, n2, straddlingCurve)
    #end init

    def add_edge(self, n : AbstractDualNode, n2 : AbstractDualNode, straddlingCurve : AbstractDualCurve):
        e = AbstractDualEdge(n, n2, straddlingCurve)
        n.incidentEdges.add(e)
        n2.incidentEdges.add(e)
        edges.add(e)
    #end add_edge

    def remove(self, e : AbstractDualEdge):
        e.fr.removeEdge(e)
        e.to.removeEdge(e)
        edges.remove(e)
    #end remove

    def remove(self, n : AbstractDualNode):
        while len(n.incidentEdges) is not 0:
            self.remove(self, n.incidentEdges.get(0))
        nodes.remove(n)
    #end remove

    def getLowDegreeEdge(self):
        pass