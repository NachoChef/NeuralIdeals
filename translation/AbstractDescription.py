'''
import java.util.HashMap;                       dictionary
import java.util.Iterator;                      iter()
import java.util.Set;                           tuple
import java.util.StringTokenizer;               re.split()
import java.util.TreeSet;                       sorted() 
'''
import re

class AbstractDescription:
    m_contours = list() #TreeSet<AbstractCurve>
    m_zones = list() #TreeSet<AbstractCurve>

    def __init__(self, contours : tuple, zones : tuple):
        self.m_contours = list(contours)
        self.m_zones = list(zones)
    #end init

    def getFirstCountour(self):
        if len(self.m_contours) is 0:
            return None
        else:
            return self.m_contours[0]
    #end getFirstCountour

    def getLastContour(self):
        if len(self.m_contours) is 0:
            return None
        else:
            return self.m_contours[-1]
    #end getLastContour

    def getContourIterator(self):
        return iter(self.m_contours)
    #end getCountourIterator

    def getNumContours(self):
        return len(self.m_contours)
    #end getNumCountours

    def getZoneIterator(self):
        return iter(self.m_zones)
    #end getZoneIterator

    def getCopyOfContours(self):
        return list(self.m_contours)
    #end getCopyOfCountours

    def getCopyOfZones(self):
        return list(self.m_zones)
    #end getCopyOfZones

    def makeForTesting(self, s : str):
        ad_zones = OrderedDict()
        ad_zones.append() #no idea
        #more stuff, think just for testing

    def one_of_multiple_instances(self, c : AbstractCurve):
        for cc in m_contours:
            if cc not c and cc.matches_label(c):
                return True
        return False

    def print_contour(self, c : AbsractCurve):
        if self.one_of_multiple_instances(c):
            pass
    #not sure if need

    def getNumZones(self):
        return len(self.m_zones)
    #end getNumZones

    def checksum(self):
        scaling, result = 2.1, 0.0
        for c in m_contours:
            result += c.checksum() * scaling
            scaling += 0.07
            scaling += 0.05
            for z in m_zones:
                if z.is_in(c):
                    result += z.checksum() * scaling
                    scaling += 0.09
        return result
    #end checksum

    def includesLabel(self, l : CurveLabel):
        for c in m_contours:
            if c.getLabel() is l:
                return True
        return False

    def hasLabelEquivalentZone(self, z : AbstractBasicRegion):
        for zone in m_zones:
            if zone.isLabelEquivalent(z):
                return True
        return False
    