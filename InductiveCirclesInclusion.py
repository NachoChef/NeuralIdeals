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

