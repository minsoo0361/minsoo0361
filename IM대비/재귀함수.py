import sys
input = sys.stdin.readline
N = int(input())
arr = [0, 1, 1]
for i in range(2, N):
    arr.append(arr[i-1]+arr[i])
print(arr[N])


