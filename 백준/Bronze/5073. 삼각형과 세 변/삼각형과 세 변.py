while True :
    tri = list(map(int, input().split()))
    tri.sort()
    if tri[0] == tri[1] == tri[2] == 0:
        break
    elif tri[2] >= tri[0] + tri[1]:
        print('Invalid')
    elif tri[0] == tri[1] == tri[2]:
        print('Equilateral')
    elif tri[0] == tri[1] or tri[0] == tri[2] or tri[1] == tri[2]:
        print('Isosceles')
    elif tri[0] != tri[1] and tri[0] != tri[2] and tri[1] != tri[2]:
        print('Scalene')
