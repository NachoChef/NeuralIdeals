import inspect, types
# -*- coding: utf-8 -*-

"""

Examples of NeuralCode

AUTHORS:

- Ethan Petersen (2015-09) [initial version]
- Justin Jones (2017-08) [visualization update]

This file constructs some examples of NeuralCodes.

The examples are accessible by typing: ``neuralcodes.example()``

"""

class NeuralCodeExamples():

    r"""

    Some examples of neuralcodes.

    Here are the available examples; you can also type

    ``neuralcodes.``  and hit tab to get a list:

    - :meth:`Canonical`

    - :meth:`Factored_Canonical`

    - :meth:`Groebner`

    - :meth:`RF_Structure`

    EXAMPLES::

        sage: nc = neuralcodes.Canonical()

        Ideal (x1*x2, x0*x1 + x0, x1*x2 + x1 + x2 + 1, x0*x2) of Multivariate Polynomial Ring in x0, x1, x2 over Finite Field of size 2


        sage: f = neuralcodes.Factored_Canonical()

        [x2 * x1, (x1 + 1) * x0, (x2 + 1) * (x1 + 1), x2 * x0]

        sage: g = neuralcodes.Groebner()

        Ideal (x0*x2, x1 + x2 + 1) of Multivariate Polynomial Ring in x0, x1, x2 over Finite Field of size 2


        sage: rf = neuralcodes.RF_Structure()

        Intersection of U_['2', '1'] is empty

    	Intersection of U_['0'] is a subset of Union of U_['1']

    	X = Union of U_['2', '1']

    	Intersection of U_['2', '0'] is empty

    """

    def __call__(self):

        r"""

        If neuralcodes() is executed, return a helpful message.

        INPUT:

        None

        OUTPUT:

        None

        EXAMPLES::

            sage: neuralcodes()

            Try neuralcodes.FOO() where FOO is in the list:

                Canonical, Factored_Canonical, Groebner, RF_Structure

        """

        print 'Try neuralcodes.FOO() where FOO is in the list:\n'

        print 'Canonical, Factored_Canonical, Groebner, RF_Structure, General_Graph, Arc_Visualize, Line_Visualize, Circle_visualize, Generate_Codes, Verify_Canonical'

    def Canonical(self):

        """

        The canonical form of the ideal corresponding to ['001','010','110'].

        INPUT:

        None

        OUTPUT:

        - Ideal

        EXAMPLES::

            sage: s = neuralcodes.Canonical()

            Ideal (x1*x2, x0*x1 + x0, x1*x2 + x1 + x2 + 1, x0*x2) of Multivariate Polynomial Ring in x0, x1, x2 over Finite Field of size 2

        """

        print 'Input:\n' +  'nc = NeuralCode([\'001\',\'010\',\'110\'])\n' + 'nc.canonical()\n\n' + 'Output:'

        nc = NeuralCode(['001','010','110'])

        return nc.canonical()

    def Factored_Canonical(self):

        """

        The factored canonical form of the ideal corresponding to ['001','010','110'].

        INPUT:

        None

        OUTPUT:

        - List

        EXAMPLES::

            sage: s = neuralcodes.factored_canonical()

            [x2 * x1, (x1 + 1) * x0, (x2 + 1) * (x1 + 1), x2 * x0]

        """

        print 'Input:\n' +  'nc = NeuralCode([\'001\',\'010\',\'110\'])\n' + 'nc.factored_canonical()\n\n' + 'Output:' 

        nc = NeuralCode(['001','010','110'])

        return nc.factored_canonical()



    def Groebner(self):

        """

        The groebner basis of the ideal corresponding to ['001','010','110'].

        INPUT:

        None

        OUTPUT:

        - Ideal

        EXAMPLES::

            sage: s = neuralcodes.groebner_basis()

            [x2 * x1, (x1 + 1) * x0, (x2 + 1) * (x1 + 1), x2 * x0]

        """

        print 'Input:\n' +  'nc = NeuralCode([\'001\',\'010\',\'110\'])\n' + 'nc.groebner_basis()\n\n' + 'Output:'

        nc = NeuralCode(['001','010','110'])

        return nc.groebner_basis()



    def RF_Structure(self):

        """

        The RF structure corresponding to ['001','010','110'].

        INPUT:

        None

        OUTPUT:

        None

        EXAMPLES::

            sage: s = neuralcodes.canonical_RF_structure()

            Intersection of U_['2', '1'] is empty

    		Intersection of U_['0'] is a subset of Union of U_['1']

    		X = Union of U_['2', '1']

    		Intersection of U_['2', '0'] is empty

        """

        print 'Input:\n' +  'nc = NeuralCode([\'001\',\'010\',\'110\'])\n' + 'nc.canonical_RF_structure()\n\n' + 'Output:'

        nc = NeuralCode(['001','010','110'])

        return nc.canonical_RF_structure()


    def General_Graph(self):
        r"""

        The general graph corresponding to [x2*x1, x1*x3]

        :return: None

        """

        print 'Input:\n cf = \'[x2*x1, x1*x3]\' \n general_graph(cf, False) \n Output:'

        general_graph('[x2*x1, x1*x3]', False)


    def Arc_Visualize(self):
        r"""

        The linear arc representation of ['001','010','110'].

        :return: None

        """

        print 'Input:\n visualize([\'001\',\'010\',\'110\'], 1, True) \n Output:'

        visualize(['001','010','110'], 1, True)


    def Line_Visualize(self):
        r"""

        The linear representation of ['001','010','110'].

        :return: None

        """

        print 'Input:\n visualize([\'001\',\'010\',\'110\'], 1, False) \n Output:'

        visualize(['001', '010', '110'], 1, False)


    def Circle_Visualize(self):
        r"""

        The circular representation of ['001','010','110'].

        :return: None

        """

        print 'Input:\n visualize([\'001\',\'010\',\'110\'], 2) \n Output:'

        visualize(['001', '010', '110'], 2)


    def Generate_Codes(self):
        r"""

        Prints all possible codeword sets corresponding to n=4 and supports = 'A B AC'.

        :return: Set of codeword sets.

        """

        print 'Input:\nfor codeword_set in gen_codewords(3, \'A B AC\'): \n\tprint(codeword_set) \n Output:'

        for codeword_set in gen_codewords(3, 'A B AC'):
            print(codeword_set)


    def Verify_Canonical(self):
        r"""

        Prints the validity of the canonical [x1*x2, (x1 + 1) * (x2 + 1), x3 * (x1 - 1)].

        Then demonstrates an invalid canonical output x1, (x1 + 1) * (x2 + 1), x3 * (x1 - 1).

        :return:True \n False

        """

        print 'Input:\n verify_canonical(\'[x1*x2, (x1 + 1) * (x2 + 1), x3 * (x1 - 1)]\') \n  Output:'

        print verify_form('[x1*x2, (x1 + 1) * (x2 + 1), x3 * (x1 - 1)]')

        print 'Input:\n verify_canonical(\'x1, (x1 + 1) * (x2 + 1), x3 * (x1 - 1)\') \n  Output:'

        print verify_form('x1, (x1 + 1) * (x2 + 1), x3 * (x1 - 1)')

        
#end examples

