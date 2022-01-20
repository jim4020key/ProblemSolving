import sys
n = int(input())
array = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())
count = 0
for num in array:
    if num >= b:
        num -= b
        count += 1
    else:
        count += 1
        continue
    if num % c == 0:
        count += num // c
    else:
        count += num // c + 1

print(count)