import sys

def solve():
    s = sys.stdin.readline().strip()
    result = []
    
    # 첫 번째 문자는 항상 추출
    result.append(s[0])
    
    # 하이픈 다음 문자를 추출
    for i in range(1, len(s)):
        if s[i-1] == '-':
            result.append(s[i])
            
    print("".join(result))

if __name__ == '__main__':
    solve()