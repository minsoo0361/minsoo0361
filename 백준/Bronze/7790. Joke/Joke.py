import sys

joke_count = 0

for line in sys.stdin:
    processed_line = line.strip()
    joke_count += processed_line.count('joke') 

print(joke_count)