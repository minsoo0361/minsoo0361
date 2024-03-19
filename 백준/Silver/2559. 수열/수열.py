import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
lst = []
lst.append(sum(arr[:K]))
for i in range(N-K):
    lst.append(lst[-1] - arr[i] + arr[i+K])
print(max(lst))
