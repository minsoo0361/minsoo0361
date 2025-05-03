word = input()
arr = []
for i in range(len(word)):
    if word[i].isupper():
        arr.append(word[i].lower())
    else:
        arr.append(word[i].upper())
for i in range(len(arr)):
    print(arr[i], end = '')