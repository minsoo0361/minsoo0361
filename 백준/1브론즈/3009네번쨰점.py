x_lst = []
y_lst = []
for i in range(3):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
for k in x_lst:
    if x_lst.count(k) == 1:
        print(k, end = ' ')
for j in y_lst:
    if y_lst.count(j) == 1:
        print(j)

