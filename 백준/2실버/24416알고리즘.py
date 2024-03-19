def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)




def dp(n):
    global cnt
    
    f = [0] * (n+1)
    f[1] = f[2] = 1
   
    for i in range (3, n+1):
        f[i] = f[i-1] + f[i-2]
        cnt += 1
    return f[n]




n = int(input())
cnt = 0
print(fib(n))
dp(n)
print(cnt)