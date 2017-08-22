import re
CF = str('x3*(x0 + 1), x3*x1, x3*x2, x4*(x0 + 1), x4*x1, x4*x3')
r"""
    The code in this file was interpreted from Proposition 3.6 of the paper 'NEURAL IDEALS AND STIMULUS SPACE VISUALIZATION' by ELIZABETH GROSS, NIDA KAZI OBATAKE, AND NORA YOUNGS

    Other Contributors: Dr. Luis Garcia, Katlin Pinelli, and Alexander Farrack
"""
def checking(cfTesting, PFS):
    r"""
        This definition uses the prepared list (cfTesting) and checks to see if C is maybe k-inductively pierced and if C is not 0 inductively pierced.

            :param cfTesting: prepared list from the regexs, this is to be checked to see if it satisfies the 2 checks e.g: ['3', '1'], ['0', '3'], ['2', '3'], ['0', '4'], ['1', '4'], ['3', '4']

            :param PFS: this is the list of the different placefields in the conical form
    """
    #first check
    #needs to be no more than 1 of the same combo.
    compareTest = cfTesting[:]
    for i in range(len(compareTest) - 1, 0,-1):
        if compareTest[i] == compareTest[i-1]:
            del compareTest[i]
    if len(cfTesting) == len(compareTest):
        print("C maybe is k-inductively pierced.")
    else:
        print("C is not k-inductively pierced.")
        exit()
    # second check
    secondTest = []
    for i in range(0, len(PFS) - 1):
        for j in range(i+1, len(PFS)):
            secondTest.append([PFS[i], PFS[j]])
    #needs to have all of the codes that there
    if cfTesting != secondTest:
        print("C is not 0 inductively pierced.")
    else:
        print("C is 0 inductively pierced.")




def KZeroPierce(CF):
    """
    This definition makes a testing list out of the given CF (conical form) string, it also makes PFS, which is all placement fields that are in the CF, Then calls checking(CF, PFS).

        :param CF: String of relations in the canonical form ideal (e.g. x1x4, x1x5, x3x4, x3x5, x3(1 − x1), x5(1 − x2), x5(1 − x4))
    """
    # number to determine if there is something invalid
    CFnumber = len(CF.split(','))

    # need to check if only there is
    cfRE = re.compile('x(\d+)\*x(\d+)')
    cfTesting = cfRE.findall(CF)
    cfRE = re.compile('x(\d+)\*\(1 - x(\d+)\)')
    cfTesting += cfRE.findall(CF)
    cfRE = re.compile('x(\d+)\*\(x(\d+) \+ 1\)')
    cfTesting += cfRE.findall(CF)
    for i in range(0, len(cfTesting)):
        cfTesting[i] = sorted(cfTesting[i])

    #check to see if if placement fields have relations with themselves.
    for i in range(0, len(cfTesting)):
        if cfTesting[i][0] == cfTesting[i][1]:
            print("Invalid entry, matching placement fields for relation.")
            exit()
    # the check to see if there is an invalid entry in the CF
    if CFnumber > len(cfTesting):
        print("Invalid entry, check all codes in the Conical Form.")
        exit()
    # finding all placement fields in the conical form
    allRE = re.compile('x(\d+)')
    PFS = []
    PFS = allRE.findall(CF)
    PFS = list(set(PFS))
    PFS = sorted(PFS)
    checking(cfTesting, PFS)