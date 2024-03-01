from collections import deque

N = int(input())
arr = deque(enumerate(map(int,input().split())))
ans = []
while arr:
    idx, nm = arr.popleft()
    ans.append(idx+1)
    # nm이 양수일때, 음수일때 구분해주기
    if nm > 0:
        arr.rotate(-(nm-1))

    else:
        arr.rotate(-nm)
print(*ans)

