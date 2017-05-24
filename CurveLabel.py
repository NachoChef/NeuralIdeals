#treeset?

class CurveLabel:

    def __init__(self, label : str):
        self.m_label = label
        self.m_library = OrderedDict()
    #end init

    def clearLibrary(self):
        self.m_library.clear() #prob not clear
    #end clearLibrary

    def get(self, label : str):
        for alreadyThere in self.m_library:
            if alreadyThere.m_label == label:
                return alreadyThere
        result = CurveLabel(label)
        self.m_library.append(result) #this depends on data type
        return result
    #end get

    def compareTo(self, other : CurveLabel):
        return self.m_label.compareTo(other.m_label)
    #end compareTo

    def checksum(self):
        result, scaling = 0.0, 1.1
        for i in range(0 , len(self.m_label)):
            result += (int)(self.m_label[i] * scaling)
            scaling += 0.01
        return result
    #end checksum

    def isLabelled(self, string : str):
        return string == self.m_label
    #end isLabelled

    def getLabel(self):
        return self.m_label
    #end getLabel
