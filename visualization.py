r"""

    A collection of various implementations centered around visualizing neural ideals in Sage.
    
    A bulk of the visualization software is written in java, however various calculations and the general graph will be found in this file.
    
    These functions are designed in such a way that they this file and the jar files are all that is needed for use, independent of the rest of the NeuralIdeals package.
    
    Authors: Justin Jones        jxj037@shsu.edu
             Alexander Farrack   ajf033@shsu.edu
    
    Initial release: Aug 15, 2017 

"""

import subprocess, os
import networkx as nx
import matplotlib.pyplot as plt
import string, random, re
from itertools import permutations
from IPython.core.display import Image, display


def visualize(args, dim=1, arc=False):
    r"""
        Given a list of codewords, determines form and translates to string if necessary.
        Then launches appropriate visualization algorithm.
        Note: 2-dim won't work in CoCalc

    :param args: a list or string of codewords

    :param dim: a 1 or 2, indicating 2-dimensional or 1-dimensional

    :param arc: if True, 1 dimensional output will be as an arc, otherwise linear
                default False

    :return: None

    ex:    >>> visualize('110 010 011', 2)
           >>> visualize(['110', '010', '011'], 1, True)
    """
    if type(args) is list:
        args = translate(args)
    if dim is 2:
        subprocess.call(['java', '-jar', os.path.join(os.getcwd(), 'InductiveCircles.jar'), args])
    elif dim is 1:
        if arc:
            #subprocess.call(['java', '-jar', os.getcwd() + '/arcs.jar', args])
            process = subprocess.Popen(['java', '-jar', os.getcwd() + '/arcs.jar', args], stdout=subprocess.PIPE)
            out, err = process.communicate()
            print(out)
            html("<img src={}></img>".format('ArcRep.jpg'))
        else:
            subprocess.call(['java', '-jar', os.path.join(os.getcwd(), 'lines.jar'), args])
            html("<img src={}></img>".format('LineRep.jpg'))
#end visualize


def general_graph(CF, zero=True, name=False):
    r"""

        Given a factored canonical form, will create and display a general relationship graph.

    :param CF: The canonical form, either string or list

    :param zero: True indicates the CF is 0-based rather than 1-based

    :param name: If true, the name of the output image will be returned

    :return: Name of output png, if name=True. Otherwise nothing.

    ex:    >>> C = ['1001', '0111'. '0101']
           >>> J = NeuralCode(C)
           >>> general_graph (J.factored_canonical(), name=True)
           >>> eXaMpLe.png

    """
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
    html("<img src={}></img>".format(fname))
    if name:
        return fname
#end general_graph


def verify_form(CF):
    r"""
        Ensures all inputs in CF are valid.

    :param CF: A factored canonical input. Should be a comma delimited string of the form '[...]' as output by Sage, or '...'.

    :return: True is valid, else False

    ex:    >>> verify_form('x1*x2, x2*(1-x3)')
           >>> True
    """

    CF = str(CF)
    copyCF = CF.split(',')

    #type 1
    t1 = re.findall(r'^\[?\s?(x[0-9]*\s*?\*\s*?x[0-9](\s*?\*\s*?x[0-9]*)?)[\,|\]?$]', CF)
    #type 2
    t2 = re.findall(r'(x[0-9]*\s*?\*\s*?\(x?[0-9]*\s*?[\+|\-]\s*?x?[0-9]*\)(\s*?\*\s*?\(x?[0-9]*\s*?[\+|\-]\s*?x?[0-9]*\))?)', CF)
    #type 3
    t3 = re.findall(r'(\(x?[0-9]*\s*?[\+|\-]\s*?x?[0-9]*\)\s*\*\s*\(x?[0-9]*\s*[\+|\-]\s*x?[0-9]*\)(\s*\*\s*\(x?[0-9]*\s*[\+|\-]\s*x?[0-9]*\))?)', CF)
    forms = [i for i in [t1, t2, t3] if i]
    forms = (1 for _ in forms)

    #if length of results are less than original, then there must be some unallowed element
    return False if sum(forms) < len(copyCF) else True
#end verify_form


def translate(input):
    r"""
    
        Maps input list to a space delimited string.
        
    :param input: A list of codewords
    
    :return: A space-delimited string
    
    ex: >>>translate(['110', '101', '001'])
        >>>'110 101 001'
    """
    output = str()
    for item in input:
      output += "".join(map(str, [i + 1 for i, c in enumerate(item) if c is '1']))
      if output[-1] is not " ":
          output += " "
    return str(output)
#end translate


def gen_codewords(n, q):
    r"""
    
        Calculate all possible sets of codewords given n, supports as string
        Note: Max return size will be n!
        
    :param n:   # of neurons
    
    :param q:   string of supports
    
    :return:    list of codeword lists for easier manipulation
    
    ex:    >>> gen_codewords(2, 'A B')
           >>> [['00', '01', '10']]
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
        #we cannot cast to a set later without making frozensets
        mainOut.append(frozenset(subOut))
        
    #this step removes any duplicates
    mainOut = set(mainOut)
    
    #and we return in an easier to manage output
    return [sorted(tuple(e)) for e in mainOut]
#end gen_codewords

#end file