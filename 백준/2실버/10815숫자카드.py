N = int(input())
card = list(map(int, input().split()))
M = int(input())
nm = list(map(int, input().split()))
dic = {}
for i in range(len(card)):
    dic[card[i]] = 0
for j in nm:
    if j in dic:
        print(1, end = ' ')
    else:
        print(0, end = ' ')


