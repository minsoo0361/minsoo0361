def dfs(x):
    check_dfs[x]= True
    print(x, end = " ")
    for i in node[x]:
        if check_dfs[i] == False:
            dfs(i)
        

def bfs(x):
    check_bfs[x] = True
    queue.append(x)

    while queue:
        n = queue.pop(0)
        print(n, end = " ")
        for i in node[n]:
            if check_bfs[i] == False:
                check_bfs[i] = True
                queue.append(i)

n, m, v = map(int,input().split())
node = [[] for _ in range(n+1)]
check_dfs= [False for _ in range(n+1)]
check_bfs= [False for _ in range(n+1)]
queue = []
for _ in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)
for k in node:
    k.sort()

dfs(v)
print()
bfs(v)