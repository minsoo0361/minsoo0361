N = int(input())
word = list(input())

for _ in range(N-1):
    word_2 = input()
    for i in range(len(word)):
        if word[i] == word_2[i]:
            continue
        else:
            word[i] = "?"

print(*word, sep = "")