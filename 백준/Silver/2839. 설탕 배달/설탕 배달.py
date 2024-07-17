N = int(input())
answer = 300000
for i in range(5000):
    if N < i * 5:
        break
    tmp = N - (i * 5)
    if (tmp % 3 == 0):
        answer = min(answer, i + (tmp // 3))
if answer == 300000:
    answer = -1
print(answer)