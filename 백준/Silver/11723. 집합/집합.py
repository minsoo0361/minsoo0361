import sys
input = sys.stdin.readline
M = int(input())
S = set()
for _ in range(M):
    word = input().strip().split()
    if word[0] == 'add':
        S.add(int(word[1]))
    elif word[0] == 'remove':
        S.discard(int(word[1]))
    elif word[0] == 'check':
        if int(word[1]) in S :
            print(1)
        else:
            print(0)
    elif word[0] == 'toggle':
        if int(word[1]) in S:
            S.discard(int(word[1]))
        else:
            S.add(int(word[1]))
    elif word[0] == 'all':
        S = {i for i in range(1, 21)}
    elif word[0] == 'empty':
        S=set()