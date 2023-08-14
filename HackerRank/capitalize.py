#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])
    
       #return s.title()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')#input proper OUTPUT_PATH

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
