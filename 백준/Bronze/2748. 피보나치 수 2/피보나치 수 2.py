memo = { 1: 1, 2: 1}
def pibo(n):
    if n in memo:
        return memo[n]
    else:
        temp = pibo(n-1) + pibo(n-2)
        memo[n] = temp
        return temp
N = int(input())
print(pibo(N))

