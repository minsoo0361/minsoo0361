N = 20

grd_scr = {
        'A+' : 4.5,
        'A0' : 4.0,
        'B+' : 3.5,
        'B0' : 3.0,
        'C+' : 2.5,
        'C0' : 2.0,
        'D+' : 1.5,
        'D0' : 1.0,
        'F'  : 0
    }
total = 0
result = 0
for _ in range(N):
    sub, grade, score = input().split()
    grade = float(grade)
    if score != 'P':
        total += grade
        result += grade * grd_scr[score]
print('{:.6f}'.format(result / total))

