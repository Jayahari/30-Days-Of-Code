#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numberOfSwaps  = 0
currSwaps = 99
temp = 0

while currSwaps != 0 :
    currSwaps = 0
    for i in range(n-1):
        if (a[i] > a[i+1] ):
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            numberOfSwaps = numberOfSwaps + 1
            currSwaps = currSwaps + 1
            

print ("Array is sorted in", numberOfSwaps , "swaps.")
print ("First Element:",a[0])
print ("Last Element:",a[-1])