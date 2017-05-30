import subprocess

#subprocess.call(['java', '-jar', 'InductiveCircles.jar'])

'''
from subprocess import *

def jarWrapper(*args):
    process = Popen(['java', '-jar']+list(args), stdout=PIPE, stderr=PIPE)
    ret = []
    while process.poll() is None:
        line = process.stdout.readline()
        if line != '' and line.endswith('\n'):
            ret.append(line[:-1])
    stdout, stderr = process.communicate()
    ret += stdout.split('\n')
    if stderr != '':
        ret += stderr.split('\n')
    ret.remove('')
    return ret

args = ['myJarFile.jar', 'arg1', 'arg2', 'argN'] # Any number of args to be passed to the jar file

result = jarWrapper(*args)
'''

#given list of codewords, translate for jar
#returns 101, 110, [...] to ac, ab, [...]
def translate(input : list):
    output = ""
    for item in input:
        output += "".join(map(str, [i + 1 for i, c in enumerate(item) if c is '1']))
        output += " "
    return str(output)

print(translate(['1101', '0101', '1011', '0000', '1111']))