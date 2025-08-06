MK = list(map(int, input().split()))
MS = list(map(int, input().split()))
a = sum(MK)
b = sum(MS)
if a >= b:
    print(a)
else:
    print(b)
