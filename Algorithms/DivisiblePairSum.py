#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))

rem = [0]*k

for a_i in a:
    rem[a_i % k] += 1

count = (rem[0] * (rem[0] - 1))/2
for i in xrange(1, (k+1)/2):
    count += rem[i] * rem[k-i]

if k % 2 == 0:
    count += (rem[k/2] * (rem[k/2] - 1)) / 2

print count
