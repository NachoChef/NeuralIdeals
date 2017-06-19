import subprocess, os

def visualize(s):
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
    if type(s) is list:
        args = translate(s)
    else:
        args = s
    subprocess.call(['java', '-jar', os.getcwd() + '/InductiveCircles.jar', args])


# given list of codewords, translate for jar
# returns 101, 110, [...] to ac, ab, [...]
def translate(input):
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
    output = str()
    for item in input:
      output += "".join(map(str, [i + 1 for i, c in enumerate(item) if c is '1']))
      if output[-1] is not " ":
          output += " "
    
    return str(output).strip()


def sort(codes, iteration=0):
    r"""
        Returns a sorted list of lists, organized 1 -> 0
    :param codes: a list of binary code words
    :param iteration: the position the function will sort
    :return: a sorted code word
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
    mid = 0
    for item in codes:
        if item[iteration] == 1:
            mid += 1

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
    coords = (((x) for x in code if x == 0) for code in codes)


