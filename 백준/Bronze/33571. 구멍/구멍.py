word_dic = {'A' : 1, 'a' : 1, 'B' : 2, 'b' : 1, 'D' : 1, 'd' : 1, 'e' : 1, 'g' : 1, 'O' : 1, 'o' : 1, 'P' : 1, 'p' : 1, 'Q' : 1, 'q': 1, 'R' : 1, '@' : 1}
cnt = 0
str_input =  list(map(str, input()))
for i in range(len(str_input)):
    if str_input[i] in word_dic:
        cnt += word_dic[str_input[i]]
print(cnt)