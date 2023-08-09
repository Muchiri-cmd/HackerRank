#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if 1<=n <=100:
        result=n%2
        if result==0:#means even 
            if n in range(2,6):
                print("Not Weird")
            elif n in range(5,21):
                print("Weird")
            elif n>20:
                print("Not Weird")
        else:
            print("Weird")
    else:
        print("Kindly Enter a number between 1 and 100 iclusive")
            