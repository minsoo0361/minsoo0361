A, B = map(int, input().split())
lst = []
for i in range(-1000, 10001):
    if i *(2 * A - i) == B:
        lst = list(set([-i, -(2 * A -i)]))
print(*sorted(lst))
