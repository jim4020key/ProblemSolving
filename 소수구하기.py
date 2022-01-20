# 여러 개의 수 소수 판별 -> 에라토스테네스의 체
import math

m, n = map(int, input().split())
array = [True for i in range(1000001)]
array[1] = 0    # 1은 소수가 아니다!

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(m, n + 1):
    if array[i]:
        print(i)