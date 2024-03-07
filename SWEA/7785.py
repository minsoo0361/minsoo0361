N = int(input())
dic = {}
for _ in range(N):
    name, entrance = map(str, (input().split()))
    if entrance == 'enter':
        dic[name] = entrance
    else:
        del dic[name]
dic = sorted(dic.keys(), reverse = True)

for i in dic:
    print(i)