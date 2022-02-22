#!/bin/python3

import sys

def euler_1_brute_force(n) :
    all_n  = [i for i in range(0,n) if (i%3 == 0 or i%5 == 0 )]
    return sum(all_n)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler_1_brute_force(n))
