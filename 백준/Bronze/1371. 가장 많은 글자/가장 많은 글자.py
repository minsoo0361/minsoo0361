import sys
from collections import Counter

text = sys.stdin.read()

count = Counter(char for char in text if char.islower())

if not count:
    exit()

max_freq = max(count.values())

result = sorted([char for char, freq in count.items() if freq == max_freq])
print("".join(result))