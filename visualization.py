import subprocess, os
import networkx as nx
import matplotlib.pyplot as plt
import string, random, re
from itertools import permutations

r"""
Determines the form of input, and translates if necessary. Then launches jar implementation of visualization.
Does not work in SageCloud.

INPUT:

- ``s`` -- may be passed either as a string of space delimited neural codes, or a list of neural codes

OUTPUT:

    None

EXAMPLES:
    sage: visualize('110 010 011')
    sage: visualize(['110', '010', '011'])

"""










r"""
If passed a list of neural codes, will return a space delimited string.

INPUT:

- ``input`` -- a list of neural codes

OUTPUT:

    A space delimited string of neural codes.

EXAMPLES:
    sage:  translate(['110', '010', '011'])
    '110 010 011'

TESTS:

>>> codes = ['110', '010', '011']
>>> expected = '110 010 011'
>>> codes == expected
True

"""


def sort(codes, iteration=0):
    r"""
        Returns a sorted list of lists, organized 1 -> 0
    :param codes: a list of binary code words
    :param iteration: the position the function will sort
    :return: a 'sorted' code word
    """
    # if is it the first iteration, check to make sure contents are lists and coerce if not
    # short circuit evaluation for iteration
    if iteration == 0 and (isinstance(codes[0], int) or isinstance(codes[0], str)):
        codes = [list(code) for code in codes]

    # to make sure we don't recurse down into the sublists or exceed range
    if not (any(isinstance(code, list) for code in codes) and len(codes) > 1):
        return codes

    # descending bubble sort
    # maybe reverse for odd iterations?
    for pos in reversed(range(len(codes))):
        for subpos in range(pos):
            if codes[subpos][iteration] < codes[subpos+1][iteration]: #so 0,1 becomes 1,0 -> shift 0 to rightmost
                codes[subpos], codes[subpos+1] = codes[subpos+1], codes[subpos]

    # return (grouped ones) + (grouped zeroes)
    # so we find the slice index for the group of ones
    mid = max(i for i in range(len(codes)) if codes[i][iteration] == 1)

    # increment iteration and move to next position
    # we split the lists and sort those sublists
    iteration += 1
    return sort(codes[:mid], iteration) + sort(codes[mid:], iteration)


def is_oscillating(codes):

    for i in range(len(codes[0])-1):
        for j in range(1, len(codes)-1):
            #can be 0 1 0 or 1 0 1
            if codes[j-1][i] < codes[j][i] > codes[j+1][i] or codes[j-1][i] > codes[j][i] < codes[j+1][i]:
                return True
    return False

def fix_oscillation(codes):
    r"""

    :param codes:
    :return: boolean, codewords
    """
    # if the second set of codes are reversed then we reverse the preceding list if all upper dims are equivalent



def general_graph(CF, zero=True):
    #'[x1*x4, x1*x5, x3*x4, x3*x5, x3*(1 - x1), x5*(1 - x2), x5*(1 - x4)]'
    #split the canonical form into segments
    if type(CF) is not str:
        CF = str(CF)
    s = CF.split(',')

    #pull out all integers for each segment and store as a point
    #then sort to remove transposited duplicates
    res = (tuple(map(int, re.findall(r'x(\d+)', x))) for x in s)
    res = set((tuple(sorted(i)) for i in res))

    #we need the range to generate the complete set of all possible edges
    length = max((max(i) for i in res))
    a = 0 if zero else 1

    #now we generate the set of all possible edges, ignoring transpositions
    total = sum(([sorted((i,j)) for j in range(a, length+a) if j is not i] for i in range(a, length+a)),[])
    total = set(tuple(i) for i in total)

    #the general graph contains all possible edges not seen in the canonical form
    #construct the graph, ensure existing nodes with degree 0 are included, then draw
    G = nx.Graph()
    G.add_edges_from(list(total - res))
    for i in range(a, length+a):
        if i not in G.nodes():
            G.add_node(i)

    colors = [(random.random(), random.random(), random.random()) for _ in range(a, length+a)]
    nx.draw(G, node_color = colors, with_labels=True)
    fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5)) + '.png'
    plt.savefig(fname)
    html("<img src="+fname+"></img>")
    return fname

def verify_form(CF):
    CF = str(CF)
    t1 = re.findall(r'([x[0-9]*[\s*?\*\s*?x[0-9][\s*\*\s*x[0-9]*]?]?)', CF)
    t2 = re.findall(r'(x[0-9]*\s*?\*\s*?\(x?[0-9]*\s*?[\+|\-]\s*?x?[0-9]*\)(\s*?\*\s*?\(x?[0-9]*\s*?[\+|\-]\s*?x?[0-9]*\))?)', CF)
    t3 = re.findall(r'(\(x?[0-9]*\s*?[\+|\-]\s*?x?[0-9]*\)\s*\*\s*\(x?[0-9]*\s*[\+|\-]\s*x?[0-9]*\)(\s*\*\s*\(x?[0-9]*\s*[\+|\-]\s*x?[0-9]*\))?)', CF)
    forms = (1 for i in [t1, t2, t3] if len(i) > 0)
    return False if sum(forms) > 2 else True

def visualize(s):
    if type(s) is list:
        args = translate(s)
    else:
        args = s
    subprocess.call(['java', '-jar', os.getcwd() + '/InductiveCircles.jar', args])

#given list of codewords, translate for jar
#returns 101, 110, [...] to ac, ab, [...]
def translate(input):
    output = str()
    for item in input:
      output += "".join(map(str, [i + 1 for i, c in enumerate(item) if c is '1']))
      if output[-1] is not " ":
          output += " "
    return str(output)

def gen_codewords(n, q):
    r"""
        Calculate all possible sets of codewords given n, supp
    :param n:   # of neurons
    :param q:   string of supports
    :return:    set of codeword sets
    """
    orig = string.ascii_uppercase[:n]
    perms = [''.join(p) for p in permutations(orig)]
    mainOut = []

    for perm in perms:
        subOut = ['0' * n]
        for support in q.split():
            newE = str(perm)
            for letter in support:
                newE = str.replace(newE, letter, '1')
            newE = ''.join('0' if i.isalpha() else i for i in newE)
            subOut.append(newE)
        mainOut.append(frozenset(subOut))
    return set(mainOut)
