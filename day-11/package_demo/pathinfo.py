"""
pathinfo:

Uses pretty-print to print the sys.path variable.  sys.path contains 
a list of the places where Python will try to resolve imports. 
"""

import sys
import pprint

pprint.pprint(sys.path)
