import sys
input = sys.stdin.readline
T = 3
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        num = int(input())
        arr.append(num)
    if sum(arr) == 0:
        print(0)
    elif sum(arr) > 0:
        print('+')
    else:
        print('-')