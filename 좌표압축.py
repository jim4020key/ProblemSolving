# 시간초과 -> dict
import sys
_input = sys.stdin.readline
n = int(input())
array = list(map(int, _input().split()))
array_t = list(sorted(set(array)))
dic = {array_t[i]: i for i in range(len(array_t))}

for i in array:
    print(dic[i], end=' ')