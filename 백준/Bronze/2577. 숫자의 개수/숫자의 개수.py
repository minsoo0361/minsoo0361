A = int(input())
B = int(input())
C = int(input())
Z = list(map(int, str(A*B*C)))

for i in range(0, 10):
    print(Z.count(i))
