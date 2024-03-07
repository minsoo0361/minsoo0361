N = int(input())
card = list(map(int, input().split()))
M = int(input())
nm = list(map(int, input().split()))
dic = {}
for i in range(len(card)):
    if card[i] in dic:
        dic[card[i]] += 1
    else:
        dic[card[i]] = 1
for j in nm:
    if j in dic:

        print(dic[j], end = ' ')
    else:
        print(0, end = ' ')


