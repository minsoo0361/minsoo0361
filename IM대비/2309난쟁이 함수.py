N = 9
def solve():
    num = sum(lst) - 100
    for i in range(N-1):
        for j in range(i+1, N):
            if lst[i] + lst[j] == num:
                return lst[i], lst[j]


lst = [int(input())for _ in range(9)]

n , m = solve()     # 9명중에 짜가 난쟁이 2명 고르는 작업
for i in sorted(lst):
    if i != n and i != m:
        print(i)