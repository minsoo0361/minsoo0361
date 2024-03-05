def fibo(a):
    # 기저조건
    if a == 1:
        return 1
    elif a == 0:
        return 0
    # 재귀조건
    else:
        return fibo(a-1) + fibo(a-2)

N = int(input())
print(fibo(N))

