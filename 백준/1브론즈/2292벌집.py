N = int(input())
if N == 1:
    cnt = 1
else:
    for n in range(1, 20000):
        if 3 * n * (n-1) + 2 <= N and N <= 3 * (n-1) * (n+2) + 7:
            cnt = n + 1
            break
print(cnt)