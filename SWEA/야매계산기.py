import sys
sys.stdin = open('input.txt', 'r')
T = 10
for tc in range(1, T+1):
    N = int(input())
    infix = input().rstrip()
    result = sum(list(map(int, infix.split('+'))))
    print(result)