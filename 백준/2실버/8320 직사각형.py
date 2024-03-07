import math
N = int(input())
# cnt = 0
# for i in range(1, N + 1):
#     for j in range(i, N + 1):
#         if i * j <= N:
#             cnt += 1
# print(cnt)
ans = N
for i in range(2, N+1):
    n = N // i - (i-1)
    if n < 1:
        break
    ans += n
print(ans)