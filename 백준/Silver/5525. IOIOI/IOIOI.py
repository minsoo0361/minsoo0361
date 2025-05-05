N = int(input())
M = int(input())
S = list(input())

cnt = 0
i = 0
pattern_count = 0

while i < M - 1:
    if S[i] == 'I' and S[i + 1] == 'O' and i + 2 < M and S[i + 2] == 'I':
        pattern_count += 1
        i += 2
        if pattern_count == N:
            cnt += 1
            pattern_count -= 1
    else:
        pattern_count = 0
        i += 1

print(cnt)
