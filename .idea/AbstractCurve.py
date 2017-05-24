#import debug?

class AbstractCurve:
    self.id = 0
    CurveLabel m_label
    m_id = int()

    def __init__(self, label : CurveLabel):
        self.id++
        self.m_id = id
        self.m_label = label
    #end init

    def getLabel(self):
        return self.m_label
    #end getLabel

    def clone(self):
        return AbstractCurve(m_label)
    #end cone

    def compareTo(self, o : AbstractCurve):
        tmp = m_label.compareTo(o.m_label)
        if tmp not 0:
            return tmp
        this_id = self.m_id
        other_id = o.m_id
        #return (this_id < other_id) ? -1 : (this_id == other_id) ? 0 : 1;
        if this_id < other_id:
            return -1
        elif this_is is other_id:
            return 0
        else:
            return 1
    #end compareTo

    def matches_label(self, c : AbstractCurve):
        return (self.m_label == c.m_label)
    #end matches_label

    def reset_id_counter(self):
        self.id = 0
    #end reset_id_counter