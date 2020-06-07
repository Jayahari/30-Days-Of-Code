#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    iStr = list (bin(n))
    iCount = 1
    iMax = 0
    for i in range(2,len(iStr)-1) :
        if iStr[i] == '1' and iStr[i+1] == '1' :
            iCount = iCount + 1
        else :
            iCount = 1
        if iCount > iMax : iMax = iCount
    print (iMax)



