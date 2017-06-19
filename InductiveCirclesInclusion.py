import subprocess, os

def visualize(s):
    r"""
    Determines the form of input, and translates if necessary. Then launches jar implementation of visualization.

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

#given list of codewords, translate for jar
#returns 101, 110, [...] to ac, ab, [...]
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

    :param codes:
    :param iteration:
    :return:
    """
    if not (any(isinstance(code, list) for code in codes) and len(codes) > 1):
        print("EXIT")
        return codes
    for pos in reversed(range(len(codes))):
        for subpos in range(pos):
            if codes[subpos][iteration] < codes[subpos+1][iteration]: #so 0,1 becomes 1,0 -> shift 0 to rightmost
                codes[subpos], codes[subpos+1] = codes[subpos+1], codes[subpos]
    # return (grouped ones) + (grouped zeroes)
    mid = 0
    for item in codes:
        if item[iteration] == 1:
            mid += 1
    iteration += 1
    return codes
    #return sort(codes[0:mid+1], iteration) + sort(codes[mid+1:], iteration)