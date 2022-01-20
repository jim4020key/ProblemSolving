# 0의 개수와 1의 개수가 각각 피보나치수열
import sys
_input = sys.stdin.readline

T = int(_input())
zero = [1, 0]   # 0의 개수
one = [0, 1]    # 1의 개수

for i in range(2, 41):
    zero.append(zero[i - 1] + zero[i - 2])
    one.append(one[i - 1] + one[i - 2])

for _ in range(T):
    n = int(_input())
    print(zero[n], one[n])

'''
cache = {0: [1, 0], 1: [0, 1]}
for i in range(2, 41):
    cache[i] = [cache[i-2][j] + cache[i-1][j] for j in range(2)]

T = int(input())
for _ in range(T):
    print(' '.join(map(str, cache[int(_input())])))
'''