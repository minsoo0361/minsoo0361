num = 123123
lst = [0]*12
for i in range(6):
    lst[num % 10] += 1
    num //= 10
k = 0
tri = run = 0
while k < 10:
    if lst[k] == 6:
        lst[k] -= 6
        tri += 2
    if lst[k] >= 3:
        lst[k] -= 3
        tri += 1
    k += 1
k = 0
while k < 10:
    if lst[k] == 2 and lst[k+1] ==2 and lst[k+2] ==2:
        lst[k] -= 2
        lst[k+1] -= 2
        lst[k+2] -= 2
        run +=2
    if lst[k] == 1 and lst[k+1] == 1 and lst[k+2] == 1:
        lst[k] -= 1
        lst[k+1] -= 1
        lst[k+2] -= 1
        run += 1
    k +=1
if run + tri == 2:
    print('baby-gin')
else:
    print('non-baby-gin')



