import sys
sys.stdin = open('GNS_test_input.txt', 'r')
num_a = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for test_case in range(1,T+1):
    temp = input()
    cnt = [0]*10
    arr = list(map(str, input().split()))

    for i in arr:
        for j in range(10):
            if i == num_a[j]:
                cnt[j] += 1
    print(f'#{test_case}')
    for i in range(10):
        for j in range(cnt[i]):
            print(num_a[i], end = ' ')
    print()



