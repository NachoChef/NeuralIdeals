class AbstractDualEdge:
    def __init__(self, fr : AbstractDualNode, to : AbstractDualNode, label : AbstractCurve):
        self.fr = fr
        self.to = to
        self.label = label
    #end init
        
