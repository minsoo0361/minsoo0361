import sys
input = sys.stdin.readline
N = int(input())
arr = []
cnt = 0
for _ in range(N):
    arr.append(int(input()))
arr.sort()
print(round(sum(arr) / N))
print(arr[N//2])
dic = dict()
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
mx = max(dic.values())
mx_lst = []
for i in dic:
    if mx == dic[i]:
        mx_lst.append(i)
if len(mx_lst) > 1:
    print(mx_lst[1])
elif len(mx_lst) == 1:
    print(mx_lst[0])
print(max(arr)-min(arr))



