# N = int(input())
# lst = [[0] * 7 for _ in range(2)]
# t1 = N
# for i in range(4):
#     lst[0][i] = t1
#     t1 += 1
# t2 = N
# for i in range(6, 2, -1):
#     lst[1][i] = t2
#     t2 -= 1
# print(lst[0])
# print(lst[1])
#
a = []
for i in range(1, 101):
    a.append(i)
b = int(((a[0]+a[-1])*len(a))/2)
print(b)
