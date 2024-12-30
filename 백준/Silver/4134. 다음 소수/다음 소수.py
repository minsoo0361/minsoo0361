import sys
import math

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input())
    if num <= 1:
        print(2)
        continue
    
    # 소수 판별 반복
    while True:
        is_prime = True  # 기본적으로 소수라 가정
        if num % 2 == 0 and num > 2:  # 짝수는 소수가 아님 (2 제외)
            num += 1
            continue
        limit = int(math.sqrt(num)) + 1
        for i in range(2, limit):
            if num % i == 0:
                is_prime = False  # 소수가 아님
                break
        if is_prime:
            print(num)  # 첫 번째 소수 출력
            break
        num += 1  # 다음 숫자로 이동
