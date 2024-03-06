import sys
input = sys.stdin.readline

N = int(input())
lst = set()

cnt = 0
for i in range(N):
    chat = input().rstrip()
    if chat == 'ENTER':
        lst = set()

    elif chat not in lst:

        cnt += 1
        lst.add(chat)
print(cnt)


