import sys
input = sys.stdin.readline
L = int(input())
N = int(input())
arr = []
tmp = [0] * (L+1)
answer = []
lst = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
for i in range(1, N + 1):
    cnt = 0
    cnt += (arr[i-1][1] - arr[i-1][0] + 1)
    answer.append(cnt)
    crt = 0
    for j in range(arr[i-1][0]-1, arr[i-1][1]):
        if tmp[j] == False:
            tmp[j] += i
            crt += 1
    lst.append(crt)
for k in range(len(answer)):
    if answer[k] == max(answer):
        print(k+1)
        break
for u in range(len(lst)):
    if lst[u] == max(lst):
        print(u+1)
        break