#!/bin/python
import sys
n = int(raw_input().strip())
ans = 0
while(n>0):
    n &= n>>1
    ans += 1
print ans
