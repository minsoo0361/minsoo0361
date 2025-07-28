word = ['C','A','M','B','R','I','D','G','E']
r = input()
arr = []
for i in r:
    if i in word:
        continue
    else:
        arr.append(i)
for i in arr:
    print(i, end = '')