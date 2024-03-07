import math
N = int(input())
tree_lst = []
nm = []
for _ in range(N):
    tree_lst.append(int(input()))
for i in range(1, N):
    nm.append(tree_lst[i] - tree_lst[i-1])
arr = list(set(nm))
min_nm = math.gcd(*arr)
tree_nm = []
for k in range(1, N):
    tree_nm.append(((tree_lst[k]-tree_lst[k-1])// min_nm) -1)
print(sum(tree_nm))
