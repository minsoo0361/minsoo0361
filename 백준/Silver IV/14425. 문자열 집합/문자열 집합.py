N, M = map(int, input().split())
cnt = 0
s = set()
for _ in range(N):
    s_word = input()
    s.add(s_word)

for _ in range(M):
    pres_word = input()
    if pres_word in s:
        cnt +=1
print(cnt)

