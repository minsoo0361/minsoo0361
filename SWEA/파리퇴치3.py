result = []
a = str(123456789)
for i in range(0, len(a), 4):
    result.append(a[i:i+4])
print(result)
