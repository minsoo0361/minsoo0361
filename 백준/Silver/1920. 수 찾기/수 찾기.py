import sys
input = sys.stdin.readline
input()
arr = list(set(map(int, input().split())))
input()
nm = list(map(int, input().split()))
arr.sort()
for i in nm:
    if i in arr:
        print(1)
    else:
        print(0)