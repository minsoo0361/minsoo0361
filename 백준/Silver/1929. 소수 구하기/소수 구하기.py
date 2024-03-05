import math
import sys
input = sys.stdin.readline


def prime(a):
    if a == 1:
        return False
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            return False
    return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if prime(i) == True:
        print(i)



