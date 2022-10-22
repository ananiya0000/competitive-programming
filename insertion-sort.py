#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    num=arr[-1]
    i=1
    while(i<n):
        if(arr[n-i-1]>num):
            arr[n-i]=arr[n-i-1]
            print(*arr)
        elif(arr[n-i-1]<num):
            arr[n-i]=num
            print(*arr)
            break
        if(n-i-1==0):
            arr[0]=num
            print(*arr)
            break
        i=i+1

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
