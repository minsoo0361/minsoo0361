arr = list(map(str, input()))
length = 10
for i in range(1, len(arr)):
    if arr[i-1] == arr[i]:
        length += 5
    else:
        length += 10
print(length)