# 시간초과 -> REVERSE의 횟수 줄이기
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input()
    p = p.replace("RR", "")
    n = int(input())
    x = input().rstrip()[1:-1].split(",")
    if x[0] == '': x = deque()
    else: x = deque(x)

    error = 0
    reverse = 0
    for i in range(len(p)):
        if p[i] == "R":
            reverse += 1
        elif p[i] == "D":
            if len(x) == 0:
                print("error")
                error = 1
                break
            else:
                if reverse%2 == 0:
                    x.popleft()
                else:
                    x.pop()

    if not error:
        if reverse % 2 != 0: x.reverse()
        print('[', end='')
        print(*x, sep=',', end='')
        print(']')
