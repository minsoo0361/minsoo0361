import sys
input = sys.stdin.readline
k, r, n = input().split()
N = int(n)
change = [['A', 0],['B', 1], ['C', 2], ['D', 3], ['E', 4], ['F', 5], ['G', 6], ['H', 7]]
K_x, K_y = int(k[1]), k[0]
R_x, R_y = int(r[1]), r[0]
K_x = 8 - K_x
R_x = 8 - R_x
for i in range(len(change)):
    if K_y == change[i][0]:
        K_y = change[i][1]
    if R_y == change[i][0]:
        R_y = change[i][1]

for k in range(N):
    dir = input().rstrip()
    if dir == 'R':
        if 0 <= K_y + 1 < 8:
            K_y += 1
            if K_x == R_x and K_y == R_y :
                if 0 <= R_y +1 < 8:
                    R_y += 1
                else:
                    K_y -= 1
    elif dir == 'L':
        if 0 <= K_y - 1 < 8:
            K_y -= 1
            if K_x == R_x and K_y == R_y :
                if 0 <= R_y -1 < 8:
                    R_y -= 1
                else:
                    K_y += 1
    elif dir == 'B':
        if 0 <= K_x + 1< 8:
            K_x += 1
            if K_x == R_x and K_y == R_y:
                if 0 <= R_x + 1< 8:
                    R_x += 1
                else:
                    K_x -= 1
    elif dir == 'T':
        if 0 <= K_x - 1 < 8:
            K_x -= 1
            if K_x == R_x and K_y == R_y:
                if 0 <= R_x -1< 8:
                    R_x -= 1
                else:
                    K_x += 1
    elif dir == 'RT':
        if 0 <= K_x -1< 8 and 0 <= K_y +1 < 8:
            K_x -= 1
            K_y += 1
            if K_x == R_x and K_y == R_y:
                if 0 <= R_x - 1 < 8 and 0 <= R_y + 1 < 8:
                    R_x -= 1
                    R_y += 1
                else:
                    K_x += 1
                    K_y -= 1
    elif dir == 'LT':
        if 0 <= K_x -1< 8 and 0 <= K_y -1< 8:
            K_x -= 1
            K_y -= 1
            if K_x == R_x and K_y == R_y:
                if 0 <= R_x - 1 < 8 and 0 <= R_y - 1 <8:
                    R_x -= 1
                    R_y -= 1
                else:
                    K_x += 1
                    K_y += 1

    elif dir == 'RB':
        if 0 <= K_x + 1< 8 and 0 <= K_y + 1 < 8:
            K_x += 1
            K_y += 1
            if K_x == R_x and K_y == R_y:
                if 0 <= R_x + 1 < 8 and 0 <= R_y + 1 <8:
                    R_x += 1
                    R_y += 1
                else:
                    K_x -= 1
                    K_y -= 1
    elif dir == 'LB':
        if 0 <= K_x +1 < 8 and 0 <= K_y - 1< 8:
            K_x += 1
            K_y -= 1
            if K_x == R_x and K_y == R_y:
                if 0 <= R_x + 1 < 8 and 0 <= R_y - 1 < 8:
                    R_x += 1
                    R_y -= 1
                else:
                    K_x -= 1
                    K_y += 1
RealK_x = 8 - K_x
RealR_x = 8 - R_x
for i in range(len(change)):
    if K_y == change[i][1]:
        RealK_y = change[i][0]
    if R_y == change[i][1]:
        RealR_y = change[i][0]
RK = [RealK_y, RealK_x]
for i in RK:
    print(i, end='')
print()
RR = [RealR_y, RealR_x]
for i in RR:
    print(i, end ='')


