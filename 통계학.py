import sys
from collections import Counter
array = []
n = int(input())
for _ in range(n):
    array.append(int(sys.stdin.readline().rstrip()))

# 최빈값 -> counter
# 여러개가 있을 때는 최빈값 중 두 번째로 작은 값을 출력한다.
counter = Counter(array)
freq_items = [k for k, v in counter.items() if max(counter.values()) == v]
if len(freq_items) == 1:
    freq = freq_items[0]
else:
    freq_items.sort()
    freq = freq_items[1]

ave = sum(array)/n
array.sort()
med = array[n//2]
ran = max(array) - min(array)

print(round(ave))
print(med)
print(freq)
print(ran)
