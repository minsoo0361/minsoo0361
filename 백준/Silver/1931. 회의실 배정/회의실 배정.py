import sys
input = sys.stdin.readline
N = int(input())
arr = [] * (N + 1)
cnt = 1
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort(key = lambda x : (x[1],x[0]))

answer = arr[0][1]
for i in range(1, N):
    if answer <= arr[i][0]:
        answer = arr[i][1]
        cnt +=1
print(cnt)


