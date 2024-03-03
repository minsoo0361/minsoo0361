N = int(input())

A = list(map(int, input().split()))
B, C = map(int, input().split())
total = 0
cnt = 1
for i in range(N):
    if B > A[i]:
        total += cnt
    else:
        t = (A[i] - B) // C
        r = (A[i] - B) % C
        if r == 0 :
            total += cnt + t
    
        else:
            total += cnt + t + 1

print(total)
