#!/bin/python3

import sys

def euler_1_brute_force(n) :
    all_n  = [i for i in range(0,n) if (i%3 == 0 or i%5 == 0 )]
    return sum(all_n)


def calculate_sum(a, N):
    # sum of first m natural numbers
    sum = ((N-1)//a) * (((N-1)//a) + 1) // 2
    # sum of multiples
    ans = a * sum
    return ans
    
def euler_1_optimized(n) : 
    return int(calculate_sum(3,n) + calculate_sum(5,n) - calculate_sum(15,n))

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler_1_optimized(n))
