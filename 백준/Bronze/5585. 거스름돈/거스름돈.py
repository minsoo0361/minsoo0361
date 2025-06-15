money = 1000 - int(input())
answer = 0
while money > 0:
    cnt = 0
    if money >= 500:
        cnt += money // 500
        money = money - cnt * 500
        answer += cnt
    elif money >= 100:
        cnt += money // 100
        money = money - cnt * 100
        answer += cnt
    elif money >= 50:
        cnt += money // 50
        money = money - cnt * 50
        answer += cnt
    elif money >= 10:
        cnt += money // 10
        money = money - cnt * 10
        answer += cnt
    elif money >= 5:
        cnt += money // 5
        money = money - cnt * 5
        answer += cnt
    elif money >= 1:
        cnt += money // 1
        money = money - cnt * 1
        answer += cnt
print(answer)


