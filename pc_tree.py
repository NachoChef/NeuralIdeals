"""
A python translation and adaptation of the C++ PC tree implementation found at
    https://github.com/kwmichaelluk/pc-tree/
by Michael Luk & Michael Zhou.

TODO:
    test implemented data structures
"""


from enum import Enum
import ctypes

class pc_tree:

    ########################################
    #data structures
    class PClabel(Enum):
        EMPTY = 0
        PARTIAL = 1
        FULL = 2
    #end PClabel

    class Pnode:
        def __init__(self):
            self.parentArc = None
    #end Pnode

    class PCarc:
        def __init__(self):
            #type PCarc
            self.a, self.b, self.twin, self.yPnode = None, None, None, None
            self.yParent = bool()
            self.label = PClabel.EMPTY
    #end PCarc

    ########################################

    def __init__(self, m, row, col):
        self.leaves = col
        self.M = list()
        for i in range(row):
            self.M[i] = col

        for i in range(row):
            for j in range(col):
                self.M[i][j] = m[i][j] #or is it [j][i]

        self.initializeTree()

        for i in range(1):
            self.currRow = i
            self.partialArcs.clear()
            self.labelTree()
            self.getTerminalPath()
            self.splitTree()
            self.contractionStep()
    #end init

    def contractionStep(self):
        marked = dict()
        #problem
        currArc = newCnode
        for i in range(newCnode.degree):
            marked[currArc] = True

            if currArc.twin.degree <= 2:
                self.contractEdge(currArc)
            elif currArc.twin.yPnode is None
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
        elif edge.b.b == edge
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
        if len(terminalPath) <= 1:
            return None

        marked = dict()
        for arc in terminalPath:
            counter = 0
            currArc = arc
            while not marked[currArc]:
                marked[currArc] = True
                if currArc.twin.label == PARTIAL:
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

        sortedPath.push_back(t1)

        currArc = t1
        pr = getParent(currArc)
        isApex = False
        while not isApex:
            isApex = True
            for i in range(len(terminalPath)):
                arc = terminalPath[i]
                if isSameNode (arc, pr):
                    sortedPath.push_back(arc)
                    currArc = arcpr = getParent(currArc)
                    terminalPath.erase(terminalPath.begin() + 1)
                    isApex = False
                    break

            if isApex:
                sortedPath.push_back(currArc)

        while currArc is not t2:
            for i in len(terminalPath):
                arc = terminalPath[i]
                if isSameNode(getParent(arc), currArc):
                    sortedPath.push_back(arc)
                    currArc = arcterminalPath.erase(terminalPath.begin() + i)
                    break

        terminalPath.clear()
        terminalPath = sortedPath
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
        terminalChild = list()
        marked = dict()
        for arc in terminalPath:
            marked.clear()
            currArc = arc

            while True
                marked[currArc] = True
                if currArc.twin.label == EMPTY or currArc.twin.label == FULL:
                    terminalChild.push_back(currArc)
                    break

                currArc = currArc.b if marked[currArc.a] else currArc.a

        terminalBounds = [[None] * len(terminalPath)] * len(terminalPath)
        for i in range(len(terminalPath)):
            bounds = [None] * 4
            terminalBounds.push_back(bounds)

        for i in range(terminalPath.size()):
            arc = terminalChild[i]

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
                    elif currLabel == EMPTY:
                        terminalBounds[i][3] = currArc

                    if nextLabel == FULL:
                        terminalBounds[i][1] = nextArc
                    elif nextLabel = EMPTY:
                        terminalBounds[i][2] = nextArc

                prevArc, currArc = currArc, nextArc
                nextArc = nextArc.b if nextArc.a == prevArc else nextArc.a

        if len(terminalPath) > 1:
            for i in range(len(terminalPath)):
                for j in range(i+1, len(terminalPath)):
                    if isAdjacent(terminalPath[i], terminalPath[j]):
                        removeEdge(terminalPath[i], terminalPath[j])

        for i in range len(terminalChild):
            fullArc = PCarc()
            fullA = fullArc if i == 0 else None
            fullB = fullArc if i == (len(terminalChild)-1) else None

            if terminalBounds[i][0] is not None:
                fullArc.a = terminalBounds[i][0]
                fullArc.b = terminalBounds[i][1]

                if terminalBounds[i][2] == None:
                    if terminalBounds[i][0].a == terminalBounds[i][1]a:
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

            if i is 0

#continue



    def initiallizeTree(self):
        parent = Pnode()
        prev = NULL
        init = NULL
        # leafArcs = new PCarc*[self.numLeaves]

        for i in range(self.numLeaves):
            a = PCarc()
            b = PCarc()

            # set Twin Arcs
            b.twin = a
            a.twin = b

            # Let a be the one point to the parent
            a.yParent = true
            b.yParent = true

            # set yPnode
            a.yPnode = parent

            # leaf pointers
            leafArcs[i] = b

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
            if i == numLeaves - 1:
                a.b = init
                init.a = a

            prev = a

            if i == 0:
                rootArc = a

    def labelTree(self):
        # reset all counters and set all labels to EMPTY
        marked = dict()

        currArc = leafArcs[0]
        resetArcSet(currArc, marked)

        for i in range(numLeaves):
            if (M[self.currRow][i] == 0):
                continue
            setFullNode(leafArcs[i])

    def setFullNode(self, arc):
        if arc.label == PClabel.FULL:
            return

        marked = dict()

        arc.label = FULL
        marked[arc] = true

        IncrementCounter(arc.twin)

        currArc = arc.a

        while currArc != arc:
            currArc.label = FULL
            marked[currArc] = true
            incrementCounter(currArc.twin)

            if marked[currArc.a] == false:
                currArc = currArc.a
            else:
                currArc = currArc.b

    def storePartialArc(self, *arc):
        marked = dict()
        for a in range(partialArcs):
            mark.clear()
            currArc = a
            while not marked[currArc]:
                marked[currArc] = true
                if currArc == arc:
                    return
                currArc = currArc.b if marked[currArc.a] else currArc.a
        partialArcs.push_back(arc)

    # NEED TO LOOK AT THIS
    def resetArcSet(self, arc, marked):
        # If already marked, return
        if marked[arc] == true:
            return
        arc.fullCounter = 0
        arc.label = EMPTY
        marked[arc] = true

        # preform same thing on twin
        resetArcSet(arc.twin, marked)

        # end if there are no neighbours but itself
        if arc.a == arc:
            return
        resetArcSet(arc.a, marked)
        resetArcSet(arc.b, marked)

    def getTerminalPath(self):
        terminalPath.clear()

        if partialArcs.size() == 1:
            print("Only 1 Partial Node")
            terminalPath.push_back(partialArcs[0])
        else:
            # Intialize - Marked all partial node arcs
            for arc in range(partialArcs):
                marked[arc] = true
                # add to terminal path
                terminalPath.push_back(arc)

                currArc = arc.a
                while currArc != arc:
                    marked[curr] = true
                    if marked[currArc.a] != true:
                        currArc = currArc.a
                    else:
                        currArc = currArc.b
            potentialApex = list()
            for arc in range(partialArcs):
                # find parent
                p = getParent(arc)

                # add to terminal path
                terminal.push_back(p)

                if marked[p]:
                    # found collision
                    # store potential apex
                    potentialApex.push_back(p)

                    # pop arc
                    particalArc.erase(particalArcs.begin())

                    continue

                else:
                    marked[p] = true

                    currArc = p.a
                    while (currArc != p):
                        marked[currArc] = true
                        if marked[currArc.a] != true:
                            currArc = currArc.a
                        else:
                            currArc = currArc.b
                    # pop arc
                    particalArcs.erase(partialArcs.begin())

                    # add parent arc
                    particalArcs.push_back(p)

            terminalPathClean()

    def terminalPathClean(self):
        marked = dict()

        # determine Highest Point
        highestArc = None

        for i in range(len(terminalPath)):
            k = terminalPath[i]
            tt = True
            for q in range(terminalPath):
                if q == k:
                    continue
                if not isHigherArc(k, q):
                    tt = false
                    break

            if tt:
                highestArc = k
                highestNum = i
                break
        while not marked[currArc]:
            if currArc.twin.label == partial:
                isApex = true
                break
            marked[currArc] = true
            currArc = currArc.b if marked[currArc.a] else currArc.a

        marked.clear()
        currArc = highestArc
        if not isApex:
            numEntering = 0

            while not marked[currArc]:
                for q in range(terminalPath):
                    if q == highestArc:
                        continue
                    if isSameNode(currArc.twin, q):
                        numEntering += 1
                        break

                if numEntering >= 2:
                    isApex = true
                    break
                marked[currArc] = true
                currArc = currArc.b if marked[currArc.a] else currArc.a

        # if apex is found, then done
        if isApex:
            return
        else:
            # remove highest point and REPEAT
            terminalPath.erase(terminalPath.begin() + highestNum)
            terminalPathClean()

    def isHigherArc(self, a, b):
        marked = dict()
        currArc = a

        while not marked[currArc]:
            marked[currArc] = true

            if currArc == b:
                return True

            currArc = currArc.b if marked[currArc.a] else currArc.a

        return False

    def isSameNode(self, a, b):
        marked = dict()
        currArc = a
        while not marked[currArc]:
            marked[currArc] = true

            if currArc == b:
                return true
            currArc = currArc.b if marked[currArc.a] else currArc.a
        return false
    #end isSameNode

    def getParent(self, arc):
        if arc.yPnode != NULL & & arc.yPnode.parentArc != NULL:
            parent = arc.yPnode.parentArc
        else:
            marked = dict()

            currArc = arc
            while true:
                if currArc.twin.yParent:
                    parent = currArc.twin
                    break
                else:
                    marked[currArc] = true
                    currArc = currArc.b if marked[currArc.a] else currArc.a

                # if no parent
                if marked[currArc]:
                    print("ERROR getParent() NO PARENT")
                    parent = NULL
                    break
        return parent
