N = int(input())
for _ in range(N):
    word = input()
    if word[0].islower() == True:
        new_word = word[0].upper() + word[1:]
    else:
        new_word = word
    print(new_word)