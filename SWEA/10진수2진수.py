# 10진수 > N진수
table = {
    # 수치 -> 문자열 (수치값)
    0 : '0',
    1 : '1',
    2 : '2',
    3 : '3',
    4 : '4',
    5 : '5',
    6 : '6',
    7 : '7',
    8 : '8',
    9 : '9',
    10 : 'A',
    11 : 'B',
    12 : 'C',
    13 : 'D',
    14 : 'E',
    15 : 'F'
    # 16 진수 초과로 더 다음의 진수 만들게 되면,,,
    # 16 : 'G'...
}
def convert(num, N):
    remains = []    # 나머지들
    while num != 0:
        # 몫과 나머지를 구하는 과정
        num, r = num // N, num % N
        # 나머지는 remains 리스트에 저장..
        remains.append(r)
    for i in range(len(remains)):   
        remains[i] = table[remains[i]]
    return ''.join(remains[::-1])

print(convert(254, 16))