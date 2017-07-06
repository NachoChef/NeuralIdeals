class PCTree:
    def __init__(self, array: list):
        self.columns = array
        print("Input: " + str(self.columns))
        m, n = len(array[0]), len(array)
        #initializing nodes to a 2m+1 by m+2 matrix
        self.nodes = [[None] * (m + 1)] * 2 * n
        self.nodes[0] = [2, self.nodes[1]] + [0] * n
        self.nodes[1] = [2, self.nodes[0]] + [0] * n
        k1, k2 = 2, 2
        for i in range(m):
            if self.columns[i][0] is 0:
                self.nodes[0][k1] = self.columns[i]
                k1 += 1
            elif self.columns[i][0] is 1:
                self.nodes[1][k2] = self.columns[i]
                k2 += 1
            else:
                raise ValueError('Invalid input, not a 1 or 0')

        index = [0] * 2 * m

        for i in range(m):
            index[i] = self.columns[i]

        index[m] = self.nodes[0]
        index[m+1] = self.nodes[1]

        #non-base case implementation
        for j in range(1, n):
            isize, tsize, trsize, bsize, osize, zsize, termtag = [0] * 7
            ones, zeroes, terminal, self.tried, touching = [[0] * 2 * m] * 5
            both = [0] * m
            for i in range(2*n):
                if index[i] is not 0:
                    isize += 1

        for i in range(m):
            if index[i][j] is 1:
                ones[osize] = index[i]
                osize += 1
            elif index[i][j] is 0:
                zeroes[zsize+1] = index[i]
                zsize += 1
            else:
                raise ValueError('Invalid input, not a 1 or 0')

        for i in range(m, isize):
            onestag, zeroestag, nodestag = [False] * 3
            for k in range(1, len(index[i])):
                if index[i][k] in self.columns:
                    if index[i][k][j] is 1:
                        onestag = True
                    if index[i][k][j] is 0:
                        zeroestag = True
                else:
                    nodestag = True

            if zeroestag and onestag:
                both[bsize] = index[i]
                bsize += 1
            elif zeroestag and nodestag:
                zeroes[zsize] = index[i]
                zsize += 1
            elif onestag and nodestag:
                ones[osize] = index[i]
                osize += 1

        for i in range(m+1, isize+1):
            onestag, zerostag, nodestag, bothtag = [False] * 4
            if index[i] in zip(ones, zeroes, both):
                for k in range(1, len(index[i])):
                    if index[i][k] in ones:
                        onestag = True
                    elif index[i][k] in zeroes:
                        zeroestag = True
                    elif index[i][k] in both:
                        bothtag = True
                    else:
                        nodestag = True
                if zeroestag and nodestag:
                    both[bsize] = index[i]
                    bsize += 1
                elif zeroestag and nodestag:
                    zeroes[zsize] = index[i]
                    zsize += 1
                elif onestag and nodestag:
                    ones[osize] = index[i]
                    osize += 1
                elif bothtag and nodestag:
                    both[bsize] = index[i]
                    bsize += 1
            #determine terminal path
        if bsize is not 0:
            print("IF1")
            if bsize is 1:
                print("IF2")
                #pnode
                if both[0][0] is 2:
                    print("IF3")
                    x = 0
                    a = len(self.nodes)-1 #edited
                    for y in range(1, len(both[0])):
                        if both[0][y] in ones:
                            self.nodes[a][x] = both[0][y]
                            x += 1
                    self.nodes[a][x] = both[0]
                    x = 1
                    for y in range(1, len(both[0])):
                        if both[0][y] in zeroes:
                            both[0][x] = both[0][y]
                            x += 1
                    both[0][x] = self.nodes[a]
                #cnode
                if both[0][0] is 3:
                    print("IF4")
                    x = 1
                    a = len(self.nodes) - 1
                    zr = 0
                    for y in range(1, len(both[0])):
                        if both[0][y] in zeroes and both[0][y+1] in ones:
                            zr += 1
                        if both[0][y+1] in zeroes and both[0][y] in ones:
                            zr += 1
                        if zr >= 3:
                            raise ValueError('There is no possible arrangement.')

            else:
                print("ELSE")
                terminal[0] = both[0]
                tsize += 1
                self.traverse(both[0], both, terminal, self.tried, tsize, trsize, termtag)
        self.display()

    def traverse(self, array: list, both: list, terminal:list, tried: list, tsize: int, trsize: int, termtag: int):
        print("TRAVERSE")
        if self.checkPath():
            exit(0)
        for i in range(1, len(array)):
            if array[i] in zip(self.columns, terminal, self.tried):
                tsize += 1
                terminal[tsize] = array[i]
                self.traverse(array[i])
            elif termtag is 0 and array[i] in both:
                termtag = 1
                terminal, tried = list(), list()
                tsize, trsize = [0] * 2
                self.traverse(array)
            elif (termtag is 1 and array in both) or (len(terminal) is 1):
                raise ValueError('There is no possible arrangement.')
            else:
                trsize += 1
                tried[trsize] = terminal[tsize]
                terminal[tsize] = 0
                tsize -= 1
                self.traverse(terminal[tsize], both, terminal, tsize, trsize, termtag)

    def display(self):
        for item in self.nodes:
            if item[0] is 2:
                print(item[1])




