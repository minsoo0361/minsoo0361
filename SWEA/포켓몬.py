N, M = map(int, input().split())
dic = {}
for i in range(1, N+1):
    monster = str(input())
    dic[monster] = str(i)
    dic[str(i)] = monster
for j in range(M):
    quiz = input()
    print(dic[quiz])



