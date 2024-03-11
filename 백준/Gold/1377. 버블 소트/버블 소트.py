N = int(input())
arr = []
cnt = 0

for i in range(N):
    arr.append([int(input()), i])
arr.sort()
for i in range(N):
    if cnt <= arr[i][1] - i:
        cnt = arr[i][1] - i

print(cnt+1)






