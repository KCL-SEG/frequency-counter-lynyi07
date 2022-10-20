"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for x in items: 
        x_str= str(x)
        if frequencies.get(x_str) == None: 
            frequencies[x_str]=1;
        else: 
            frequencies[x_str] = frequencies.get(x_str)+1; 
            # Your code goes here
    return frequencies
