'''
import java.util.HashMap;                       dictionary
import java.util.Iterator;                      iter()
import java.util.Set;                           tuple
import java.util.StringTokenizer;               re split()
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
