import re

# for testing
CF = str('x3*(x0 + 1), x3*x1, x3*x2, x4*(x0 + 1), x4*x1, x4*x3')
t = CF.replace("[", "")
t = t.replace("]", "")

r"""
    The code in this file was interpreted from Proposition 3.1 of the paper 'NEURAL IDEALS AND STIMULUS SPACE VISUALIZATION' by ELIZABETH GROSS, NIDA KAZI OBATAKE, AND NORA YOUNGS

    Other Contributors: Dr. Luis Garcia, Katlin Pinelli, and Alexander Farrack
"""

def PiercingZone(CF, N):
    r"""
        Given the canonical form ideal and a given placement field
        if it has a piercing gives the piercing number and zones associated with it otherwise will state it's not a piercing.
    		(e.g. ' 0 ' is not a piercing.
                  ' 1 ' is a  2 - piercing of  ['0', '2']  identified by zone []
                  ' 2 ' is not a piercing.
                  ' 3 ' is a  0 - piercing of  []  identified by zone ['0']
                  ' 4 ' is a  1 - piercing of  ['2']  identified by zone ['0'])

    	:param CF: (List of strings): List of the relations in the canonical form ideal (e.g. [x1x4, x1x5, x3x4, x3x5, x3(1 − x1), x5(1 − x2), x5(1 − x4)])

    	:param N: (string): a single placement field

        ex: >>> PiercinZone("x3*(x3 + 1), x3*x1, x3*x2, x4*(x0 + 1), x4*x1, x4*x3", "3")
    """
    #this is the error switch, if it is not false by the end of the definition then it's not a piercing
    error = False
    aRE = re.compile('x(\d+)\*x(\d+)')
    aTesting = aRE.findall(t)
    A = []
    #using B1 and B2 to create B, keeping them in seperate lists so they can be compared
    B = []
    B1 = []
    B2 = []

    #gathering A
    for i in range(0,len(aTesting)):
        if N == aTesting[i][0]:
            A += [aTesting[i][1]]
        elif N == aTesting[i][1]:
            A += [aTesting[i][0]]

    zRE = re.compile('x(\d+)\*\(1 - x(\d+)\)')
    zTesting = zRE.findall(t)
    zRE = re.compile('x(\d+)\*\(x(\d+) \+ 1\)')
    zTesting += zRE.findall(t)

    Z = []
    C = []
    #gathering Z
    for i in range(0,len(zTesting)):
        if N == zTesting[i][0]:
            Z += [zTesting[i][1]]
        elif N == zTesting[i][1]:
            C += [zTesting[i][0]]
    #if C is not 0 then llama it's not a piercing
    if len(C) != 0:
        #print("Not a piercing, C is not 0")
        error = True
        #exit()
    #if B1 and B2 have a number in common it's not a piercing
    for i in range(0,len(B1)):
        if B1[i] in B2:
            #print("Not a piercing, matching numbers with A and Z")
            error = True
            #exit()

    #checking to see if there is invalid code in the CF
    CFCheckLength = CF.split(",")
    if len(CFCheckLength) != (len(aTesting) + len(zTesting)):
        print("Invalid entry, check all codes in the Conical Form.")
        exit()
    #checking to see matching PFS for a single relation
    for i in range(0, len(aTesting)):
        if aTesting[i][0] == aTesting[i][1]:
            print("Invalid entry, matching placement fields for a code, check Conical Form.")
            exit()
    for i in range(0, len(zTesting)):
        if zTesting[i][0] == zTesting[i][1]:
            print("Invalid entry, matching placement fields for a code, check Conical Form.")
            exit()

    allRE = re.compile('x(\d+)')
    B = []
    B = allRE.findall(t)
    B = list(set(B))
    B = sorted(B)
    if N in B:
        B.remove(N)
    for i in range(0, len(A)):
        if A[i] in B:
            B.remove(A[i])
    for i in range(0, len(Z)):
        if Z[i] in B:
            B.remove(Z[i])

    #check to see if there is any non 0s, this would imply it's not a piercing
    for i in range(0,len(aTesting)):
        if N != aTesting[i][0] and N != aTesting[i][1]:
            if aTesting[i][0] not in A and aTesting[i][1] not in A:
                #print("Not a piercing, number in list not in A (doesn't zero out)")
                error = True
        else:
            if aTesting[i][0] == N and aTesting[i][1] == N:
                #print("Number matches number given, not a piercing...")
                error = True

    for i in range(0,len(zTesting)):
        if zTesting[i][0] not in A:
            if zTesting[i][1] not in Z:
                #print("Not a piercing, number in list not in Z (doesn't zero out)")
                error = True
        else:
            if zTesting[i][1] == N:
                #print("Number matches number given, not a piercing...")
                error = True
    if error == False:
        print('\'' + str(N) + '\'' + " is a " + str(len(B)) + "- piercing of " + str(B) + " identified by zone" + str(Z))
    else:
        print('\'' + str(N) + '\'' + " is not a piercing.")
    #size of B is what k piercing it is

def PiercingZones(CF):
    r"""
        Given the canonical form ideal it takes the CF and breaks in into placement fields it has.
        it then feeds each placement field to PiercingZone to determine piercing and zones of the placement field

        :param CF: List of the relations in the canonical form ideal (e.g. [x1x4, x1x5, x3x4, x3x5, x3(1 − x1), x5(1 − x2), x5(1 − x4))

        ex: >>> PiercinZones("x3*(x3 + 1), x3*x1, x3*x2, x4*(x0 + 1), x4*x1, x4*x3")
    """

    # Placement fields list is to recursively find and use all the areas in the list
    allRE = re.compile('x(\d+)')
    PFS = []
    PFS = allRE.findall(t)
    PFS = list(set(PFS))
    PFS = sorted(PFS)
    for i in range(0,len(PFS)):
        PiercingZone(CF, PFS[i])