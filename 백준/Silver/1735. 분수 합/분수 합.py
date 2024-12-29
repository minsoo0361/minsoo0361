import sys
input = sys.stdin.readline

def gcd(A, B):
    while True:
        C = A % B
        if C == 0:
            return B
        A = B
        B = C

A, B = map(int, input().split())
C, D = map(int, input().split())

        
bunja = A*D + C*B
bunmo = B*D
gcd_ = gcd(max(bunja,bunmo), min(bunja,bunmo))

print(bunja // gcd_, bunmo // gcd_)



