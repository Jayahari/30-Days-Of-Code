#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    iMax = -65
    #iMax = None
    iSum = 0
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    for (i) in range (1,5) :
        for (j) in range (1,5) :
            iSum = arr[i][j] 
            iSum = iSum + arr[i-1][j] + arr[i-1][j-1] + arr[i-1][j+1]
            iSum = iSum + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j+1]
            if iSum > iMax : iMax = iSum
    print (iMax)
