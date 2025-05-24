import sys

joke_count = 0

for line in sys.stdin:
    processed_line = line.strip()
    
    # 여기서 핵심 변경: count() 메서드를 사용
    # processed_line 안에 'joke'가 몇 번 나타나는지 정확히 셉니다.
    joke_count += processed_line.count('joke') 

print(joke_count)