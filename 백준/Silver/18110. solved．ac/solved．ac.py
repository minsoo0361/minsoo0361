import sys

def custom_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(sys.stdin.readline())
if n == 0:
    print(0)
    exit()

arr = [int(sys.stdin.readline()) for _ in range(n)]
cut = custom_round(n * 0.15)

arr.sort()
trimmed = arr[cut:n - cut]

if not trimmed:
    print(0)
else:
    avg = custom_round(sum(trimmed) / len(trimmed))
    print(avg)
