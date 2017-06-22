"""
A python translation and adaptation of the C++ PC tree implementation found at
    https://github.com/kwmichaelluk/pc-tree/
by Michael Luk & Michael Zhou.

TODO:
    test implemented data structures
"""


from enum import Enum
import ctypes


########################################
# data structures
class PClabel(Enum):
    EMPTY = 0
    PARTIAL = 1
    FULL = 2


# end PClabel

class Pnode:
    def __init__(self):
        self.parentArc = None


# end Pnode

class PCarc:
    def __init__(self):
        # type PCarc
        self.a, self.b, self.twin, self.yPnode = None, None, None, None
        self.yParent = bool()
        self.label = PClabel.EMPTY


# end PCarc

########################################

class pc_tree:

    def __init__(self, m, row, col):
        self.numLeaves = col
        self.M = [[0] * col] * row
        '''
        for i in range(row):
            self.M[i] = int(col)
        '''
        for i in range(row):
            for j in range(col):
                self.M[i][j] = m[i][j] #or is it [j][i]
        self.leafArcs = list()
        print("INIT")
        self.initializeTree()
        self.terminalPath = list()
        self.partialArcs = list()
        self.newCnode = PCarc()
        for i in range(1):
            self.currRow = i
            print("CLEAR PARARCS")
            self.partialArcs.clear()
            print("LABELTREE")
            self.labelTree()
            print("TPATH")
            self.getTerminalPath()
            print("SPLIT")
            self.splitTree()
            print("CONTRACTION")
            self.contractionStep()
        self.terminalChild = list()
    #end init

    def contractionStep(self):
        marked = dict()
        #problem
        currArc = newCnode
        for i in range(newCnode.degree):
            marked[currArc] = True

            if currArc.twin.degree <= 2:
                self.contractEdge(currArc)
            elif currArc.twin.yPnode is None:
                self.contractEdge(currArc)

            currArc = currArc.b if marked[currArc.a] else currArc.a
    #end contractionStep

    def contractEdge(self, edge):
        if edge.a.a == edge:
            edge.a.a = edge.twin.a
        elif edge.a.b == edge:
            edge.a.b = edge.twin.a
        else:
            print("error1")

        if edge.b.a == edge:
            edge.b.a = edge.twin.b
        elif edge.b.b == edge:
            edge.b.b = edge.twin.b
        else:
            print("error2")

        if edge.twin.a.a == edge.twin:
            edge.twin.a.a = edge.a
        elif edge.twin.a.b == edge.twin:
            edge.twin.a.b = edge.a
        else:
            print("error3")

        if edge.twin.b.a == edge.twin:
            edge.twin.b.a = edge.b
        elif edge.twin.b.b == edge.twin:
            edge.twin.b.b = edge.b
        else:
            print("error4")
    #end contractEdge

    def sortTerminalPath(self):
        sortedPath = list()
        if len(self.terminalPath) <= 1:
            return None

        marked = dict()
        for arc in self.terminalPath:
            counter = 0
            currArc = arc
            while not marked[currArc]:
                marked[currArc] = True
                if currArc.twin.label == PClabel.PARTIAL:
                    counter += 1

                currArc = currArc.b if marked[currArc.a] else currArc.a

            if counter is 1:
                if t1 is None:
                    t1 = arc
                else:
                    t2 = arc

            assert(counter <= 2)

            if t1 is not None and t2 is not None:
                break

        sortedPath.append(t1)

        currArc = t1
        pr = self.getParent(currArc)
        isApex = False
        while not isApex:
            isApex = True
            for i in range(len(self.terminalPath)):
                arc = self.terminalPath[i]
                if self.isSameNode(arc, pr):
                    sortedPath.append(arc)
                    currArc = arc
                    pr = self.getParent(currArc)
                    del self.terminalPath[self.terminalPath[0] + 1]
                    isApex = False
                    break

            if isApex:
                sortedPath.append(currArc)

        while currArc is not t2:
            for i in range(len(self.terminalPath)):
                arc = self.terminalPath[i]
                if self.isSameNode(self.getParent(arc), currArc):
                    sortedPath.append(arc)
                    currArc = arc
                    del self.terminalPath[self.terminalPath[0] + i]
                    break

        self.terminalPath.clear()
        self.terminalPath = sortedPath
    #end sortTerminalPath

    def setDegree(self, node):
        marked = dict()
        currArc = node
        degree = 0
        while not marked[currArc]:
            marked[currArc] = True
            degree += 1
            currArc = currArc.b if marked[currArc.a] else currArc.a

        marked.clear()
        while not marked[currArc]:
            marked[currArc] = True
            currArc.degree = degree
            currArc = currArc.b if marked[currArc.a] else currArc.a
    #end setDegree

    def splitTree(self):
        self.sortTerminalPath()
        self.terminalChild = list()
        marked = dict()
        for arc in self.terminalPath:
            marked.clear()
            currArc = arc

            while True:
                marked[currArc] = True
                if currArc.twin.label == PClabel.EMPTY or currArc.twin.label == PClabel.FULL:
                    self.terminalChild.append(currArc)
                    break

                currArc = currArc.b if marked[currArc.a] else currArc.a

        terminalBounds = [[None] * len(self.terminalPath)] * len(self.terminalPath)
        for i in range(len(self.terminalPath)):
            bounds = [None] * 4
            terminalBounds.append(bounds)

        for i in range(len(self.terminalPath)):
            arc = self.terminalChild[i]

            nextArc = arc.a
            currArc = arc
            marked.clear()
            while not marked[currArc]:
                marked[currArc] = True
                currLabel = currArc.twin.label
                nextLabel = nextArc.twin.label

                if currLabel is not nextLabel:
                    if currlabel == FULL:
                        terminalBounds[i][0] = currArc
                    elif currLabel == PClabel.EMPTY:
                        terminalBounds[i][3] = currArc

                    if nextLabel == PClabel.FULL:
                        terminalBounds[i][1] = nextArc
                    elif nextLabel == PClabel.PClabel.EMPTY:
                        terminalBounds[i][2] = nextArc

                prevArc, currArc = currArc, nextArc
                nextArc = nextArc.b if nextArc.a == prevArc else nextArc.a

        if len(self.terminalPath) > 1:
            for i in range(len(self.terminalPath)):
                for j in range(i+1, len(self.terminalPath)):
                    if self.isAdjacent(self.terminalPath[i], self.terminalPath[j]):
                        self.removeEdge(self.terminalPath[i], self.terminalPath[j])

        for i in range(len(self.terminalChild)):
            fullArc = PCarc()
            fullA = fullArc if i == 0 else None
            fullB = fullArc if i == (len(self.terminalChild)-1) else None

            if terminalBounds[i][0] is not None:
                fullArc.a = terminalBounds[i][0]
                fullArc.b = terminalBounds[i][1]

                if terminalBounds[i][2] == None:
                    if terminalBounds[i][0].a == terminalBounds[i][1].a:
                        terminalBounds[i][0].a = fullArc
                    elif terminalBounds[i][0].b == terminalBounds[i][1]:
                        terminalBounds[i][0].b = fullArc
                    else:
                        print("ERROR TERMINAL BOUND1!")  #probably raise exception here?

                    if terminalBounds[i][1].a == terminalBounds[i][0].a:
                        terminalBounds[i][1].a = fullArc
                    elif terminalBounds[i][1].b == terminalBounds[i][0]:
                        terminalBounds[i][1].b = fullArc
                    else:
                        print("ERROR TERMINAL BOUND2!")  #probably raise exception here?
                else:
                    if terminalBounds[i][0].a == terminalBounds[i][2].a:
                        terminalBounds[i][0].a = fullArc
                    elif terminalBounds[i][0].b == terminalBounds[i][2]:
                        terminalBounds[i][0].b = fullArc
                    else:
                        print("ERROR TERMINAL BOUND3!")  #probably raise exception here?

                    if terminalBounds[i][1].a == terminalBounds[i][3].a:
                        terminalBounds[i][1].a = fullArc
                    elif terminalBounds[i][1].b == terminalBounds[i][3]:
                        terminalBounds[i][1].b = fullArc
                    else:
                        print("ERROR TERMINAL BOUND4!")  #probably raise exception here?

            fullArc.twin = PCarc()
            fullArc.twin.twin = fullArc

            if i is 0:
                initC = fullArc.twin
            else:
                fullArc.twin.a = prevC
                prevC.b = fullArc.twin

            prevC = fullArc.twin

            fullArc.yParent = False
            fullArc.twin.yParent = True

            for i in range(len(terminalChild)):
                if terminalBounds[i][0] != None:
                    self.setDegree(terminalBounds[i][0])

            if fullArc.yPnode != None:
                self.setNewPnode(fullArc)

        emptA, emptB = PCarc(), PCarc()
        for i in range(len(terminalChild)):
            fullArc = PCarc()

            if i is 0:
                emptA = fullArc

            if i == len(terminalChild)-1:
                emptB = fullArc

            if terminalBounds[i][2] != None:
                fullArc.a = terminalBounds[i][2]
                fullArc.b = terminalBounds[i][3]

                if terminalBounds[i][1] == None:
                    if terminalBounds[i][2].a == terminalBounds[i][3]:
                        terminalBounds[i][2].a = fullArc
                    elif terminalBounds[i][2].b == terminalBounds[i][3]:
                        terminalBounds[i][2].b = fullArc
                    else:
                        print("TERMINAL BOUND5")

                    if terminalBounds[i][3].a == terminalBounds[i][2]:
                        terminalBounds[i][3].a = fullArc
                    elif terminalBounds[i][3].b == terminalBounds[i][2]:
                        terminalBounds[i][3].b = fullArc
                    else:
                        print("TERMINAL BOUND6")

                else:
                    if terminalBounds[i][2].a == terminalBounds[i][0]:
                        terminalBounds[i][2].a = fullArc
                    elif terminalBounds[i][2].b == terminalBounds[i][0]:
                        terminalBounds[i][2].b = fullArc
                    else:
                        print("TERMINAL BOUND7")

                    if terminalBounds[i][3].a == terminalBounds[i][1]:
                        terminalBounds[i][3].a = fullArc
                    elif terminalBounds[i][3].b == terminalBounds[i][1]:
                        terminalBounds[i][3].b = fullArc
                    else:
                        print("TERMINAL BOUND8")

            fullArc.twin = PCarc()
            fullArc.twin.twin = fullArc

            if i is 0:
                initC = fullArc.twin
            else:
                fullArc.twin.a = prevC
                prevC.b = fullArc.twin

            prevC = fullArc.twin
            fullArc.yParent = False
            fullArc.twin.yParent = True

            for i in range(len(self.terminalChild)):
                if terminalBounds[i][2] != None:
                    self.setDegree(terminalBounds[i][2])

        fullA.twin.a = emptA.twin
        emptA.twin.a = fullA.twin

        fullB.twin.a = emptA.twin
        emptB.twin.b = fullB.twin

        newCnode = initC
        self.rootArc = newCnode
        self.setDegree(newCnode)

        assert(newCnode.degree == len(self.terminalChild) * 2)
    #end splitTree

    def setNewPnode(self, node):
        marked = dict()
        currArc = node
        newPnode = Pnode()

        while not marked[currArc]:
            marked[currArc] = True
            currArc.yPnode = newPnode
            currArc = currArc.b if marked[currArc.a] else currArc.a

        newPnode.parentArc = self.getParent(node)
    #end setNewPnode

    def isAdjacent(self, nodeA, nodeB):
        pA = self.getParent(nodeA)
        pB = self.getParent(nodeB)

        return True if self.isSameNode(pA, nodeB) or self.isSameNode(pB, nodeA) else False
    #end isAdjacent

    def removeEdge(self, nodeA, nodeB):
        marked = dict()

        currArc = nodeA
        while not marked[currArc]:
            marked[currArc] = True
            currArc = currArc.b if marked[currArc.a] else currArc.a

        currArc = nodeB
        while not marked[currArc.twin]:
            if marked[currArc]:
                print("PROBLEM removeEdge() Cannot find common edge!")

            marked[currArc] = True
            currArc = currArc.b if marked[currArc].a else currArc.a

        self.removeEdge(currArc)
    #end removeEdge

    def removeEdge(self, arc):
        prev, next = arc.a, arc.b

        if prev.a == arc:
            prev.a = next
        else:
            if prev.b != arc:
                print("WARNING! removeEdge()")
            prev.b = next

        if next.a == arc:
            next.a = prev
        else:
            if next.b != arc:
                print("WARNING removeEdge()")
            next.b = prev

        prev = arc.twin.a
        next = arc.twin.b

        if prev.a == arc.twin:
            prev.a = next
        else:
            if prev.b != arc.twin:
                print("WARNING removeEdge()")
            prev.b = next

        if next.a == arc.twin:
            next.a = prev
        else:
            if next.b != arc.twin:
                print("WARNING removeEdge()")
            next.b = prev

        del arc.twin
        del arc
    #end removeEdge(2)

    def initializeTree(self):
        parent = Pnode()
        prev = None
        init = None
        self.leafArcs = [None] * self.numLeaves

        for i in range(self.numLeaves):
            a = PCarc()
            b = PCarc()

            # set Twin Arcs
            b.twin = a
            a.twin = b

            # Let a be the one point to the parent
            a.yParent = True
            b.yParent = True

            # set yPnode
            a.yPnode = parent

            # leaf pointers
            self.leafArcs[i] = b

            # Leaf Neighbours point to self
            b.a = b
            b.b = b

            # set degree - A node is represented by its arcs
            a.degree = self.numLeaves
            b.degree = 1

            # set neighbours
            if i != 0:
                a.a = prev
                prev.b = a
            else:
                init = a

            # for end case
            if i == self.numLeaves - 1:
                a.b = init
                init.a = a

            prev = a

            if i == 0:
                self.rootArc = a

    def labelTree(self):
        # reset all counters and set all labels to PClabel.EMPTY
        marked = dict()

        currArc = self.leafArcs[0]
        self.resetArcSet(currArc, marked)

        for i in range(self.numLeaves):
            if (self.M[self.currRow][i] == 0):
                continue
            self.setFullNode(self.leafArcs[i])

    def setFullNode(self, arc):
        if arc.label == PClabel.FULL:
            return

        marked = dict()

        arc.label = PClabel.FULL
        marked[arc] = True

        IncrementCounter(arc.twin)

        currArc = arc.a

        while currArc != arc:
            currArc.label = PClabel.FULL
            marked[currArc] = True
            incrementCounter(currArc.twin)

            if marked[currArc.a] == False:
                currArc = currArc.a
            else:
                currArc = currArc.b

    def storePartialArc(self, *arc):
        marked = dict()
        for a in range(self.partialArcs):
            mark.clear()
            currArc = a
            while not marked[currArc]:
                marked[currArc] = True
                if currArc == arc:
                    return
                currArc = currArc.b if marked[currArc.a] else currArc.a
        self.partialArcs.append(arc)

    def resetArcSet(self, arc, marked):
        # If already marked, return
        if marked[arc] == True:
            return None
        arc.fullCounter = 0
        arc.label = PClabel.EMPTY
        marked[arc] = True

        # preform same thing on twin
        self.resetArcSet(arc.twin, marked)

        # end if there are no neighbours but itself
        if arc.a == arc:
            return None
        self.resetArcSet(arc.a, marked)
        self.resetArcSet(arc.b, marked)

    def getTerminalPath(self):
        self.terminalPath.clear()

        if partialArcs.size() == 1:
            print("Only 1 Partial Node")
            self.terminalPath.append(self.partialArcs[0])
        else:
            # Intialize - Marked all partial node arcs
            for arc in range(partialArcs):
                marked[arc] = True
                # add to terminal path
                self.terminalPath.append(arc)

                currArc = arc.a
                while currArc != arc:
                    marked[curr] = True
                    if marked[currArc.a] != True:
                        currArc = currArc.a
                    else:
                        currArc = currArc.b
            potentialApex = list()
            for arc in range(partialArcs):
                # find parent
                p = getParent(arc)

                # add to terminal path
                terminal.append(p)

                if marked[p]:
                    # found collision
                    # store potential apex
                    potentialApex.append(p)

                    # pop arc
                    particalArc.erase(particalArcs.begin())

                    continue

                else:
                    marked[p] = True

                    currArc = p.a
                    while (currArc != p):
                        marked[currArc] = True
                        if marked[currArc.a] != True:
                            currArc = currArc.a
                        else:
                            currArc = currArc.b
                    # pop arc
                    particalArcs.erase(partialArcs.begin())

                    # add parent arc
                    particalArcs.append(p)

            self.terminalPathClean()

    def terminalPathClean(self):
        marked = dict()

        # determine Highest Point
        highestArc = None

        for i in range(len(self.terminalPath)):
            k = self.terminalPath[i]
            tt = True
            for q in range(self.terminalPath):
                if q == k:
                    continue
                if not self.isHigherArc(k, q):
                    tt = False
                    break

            if tt:
                highestArc = k
                highestNum = i
                break
        while not marked[currArc]:
            if currArc.twin.label == PClabel.PARTIAL:
                isApex = True
                break
            marked[currArc] = True
            currArc = currArc.b if marked[currArc.a] else currArc.a

        marked.clear()
        currArc = highestArc
        if not isApex:
            numEntering = 0

            while not marked[currArc]:
                for q in range(len(self.terminalPath)):
                    if q == highestArc:
                        continue
                    if self.isSameNode(currArc.twin, q):
                        numEntering += 1
                        break

                if numEntering >= 2:
                    isApex = True
                    break
                marked[currArc] = True
                currArc = currArc.b if marked[currArc.a] else currArc.a

        # if apex is found, then done
        if isApex:
            return
        else:
            # remove highest point and REPEAT
            '''problem here'''
            self.terminalPath.erase(self.terminalPath.begin() + highestNum)
            self.terminalPathClean()

    def isHigherArc(self, a, b):
        marked = dict()
        currArc = a

        while not marked[currArc]:
            marked[currArc] = True

            if currArc == b:
                return True

            currArc = currArc.b if marked[currArc.a] else currArc.a

        return False

    def isSameNode(self, a, b):
        marked = dict()
        currArc = a
        while not marked[currArc]:
            marked[currArc] = True

            if currArc == b:
                return True
            currArc = currArc.b if marked[currArc.a] else currArc.a
        return False
    #end isSameNode

    def getParent(self, arc):
        if (arc.yPnode != None) and (arc.yPnode.parentArc != None):
            parent = arc.yPnode.parentArc
        else:
            marked = dict()

            currArc = arc
            while True:
                if currArc.twin.yParent:
                    parent = currArc.twin
                    break
                else:
                    marked[currArc] = True
                    currArc = currArc.b if marked[currArc.a] else currArc.a

                # if no parent
                if marked[currArc]:
                    print("ERROR getParent() NO PARENT")
                    parent = None
                    break
        return parent
