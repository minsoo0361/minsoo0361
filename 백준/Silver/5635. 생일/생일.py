n = int(input())
lst = []
for _ in range(n):
    name, day, month, year = map(str, input().split())
    day = int(day)
    month = int(month)
    year = int(year)
    lst.append([year, month, day, name])
sor_lst = sorted(lst, key=lambda x : (-x[0], -x[1], -x[2]))
print(sor_lst[0][3])
print(sor_lst[-1][3])