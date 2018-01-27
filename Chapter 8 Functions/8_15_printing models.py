"""
8-15 Printing Models: Put the functions from the example print_models.py 
in a seperate file called printing_functions.py. Write an import statement
at the top of print_models.py, and modify the file to use the import functions.
"""

import printing_functions as pf

unprinted_designs = ['iPhone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs[:], completed_models)
pf.show_completed_models(completed_models)