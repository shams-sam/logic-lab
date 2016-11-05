# Complete the function below.
import math

def findPair(num, arr, dict):
    found = False
    for elem in arr:
        if num%elem == 0:
            div = num/elem
            freq = dict.get(div, None)
            if (freq == 1 and div != num and div!= elem or freq > 1):
                found = True
                break
    return found

def  maxElement(arr):
    arr = sorted(arr, reverse=True)
    n = len(arr)
    found = False
    max = -1
    dict = {}
    for elem in arr:
        dict[elem] = dict.get(elem, 0) + 1
    for i in xrange(0,n-2):
        found = findPair(arr[i], arr[i+1:n], dict)
        if (found):
            max = arr[i]
            break
    return max

print maxElement([2,4,2])
