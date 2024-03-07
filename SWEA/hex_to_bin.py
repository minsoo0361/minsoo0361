# 매직 테이블 : 16진수 자릿수 -> 2진수 4자리로 변환 테이블
hx = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


# 16진수 문자열을 2진수 문자열로 바꿔주는 함수
def convert(hex_data):
    bn = ''
    for ch in hex_data:
        bn += hx[ch]
    return bn

hex_data = '01D06079861D79F99F'  # input()
bin_data = convert(hex_data)  # hex_data를 이진수에 해당하는 문자열로 변환


# 7 bit씩 묶어서 십진수로 변환
# int(bin_data[0:7], base = 2)
result = []
for idx in range(0, len(bin_data) , 7):
    result.append(int(bin_data[idx:idx+7], base = 2))     # 7bit 씩 자르고..
print(len(bin_data))
for i in result:
    print(i, ", ", end = " ")