"""Demo module to show python search path"""
import sys
import pprint

def print_path():
    """Pretty print the system path"""
    print("Printing the search path:")
    pprint.pprint(sys.path)