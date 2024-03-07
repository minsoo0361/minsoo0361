import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

a, b = list(map(int, (input().split())))
print(a * b)