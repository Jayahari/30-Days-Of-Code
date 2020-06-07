#!/bin/python3

import sys


S = input().strip()


try:
  d = int(S) 
  print (S)
except:
  print("Bad String")