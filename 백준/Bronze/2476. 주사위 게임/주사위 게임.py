N = int(input())
answer = []
for _ in range(N):
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    cnt = 0
    if lst[0] == lst[1]:
        cnt += 1
    if lst[1] == lst[2]:
        cnt += 1
    if lst[0] == lst[2]:
        cnt += 1

    if cnt == 0:
        money = lst[0] * 100
        answer.append(money)
    elif cnt == 1:
        money = (1000 + lst[1] * 100)    
        answer.append(money)
    elif cnt == 3:
        money = (10000 + lst[0] * 1000)
        answer.append(money)

print(max(answer))
