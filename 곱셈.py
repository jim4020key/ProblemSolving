# 분할 정복을 이용한 거듭제곱
# a를 b번 곱한 수를 c로 나눈 나머지를 출력
import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())

# c를 함수 안에서 처리했더니 시간초과 해결
def power(a, b):
    if b == 1:
        return a % c

    result = power(a, b//2)
    if b % 2 == 0:
        return result * result % c
    else:
        return result * result * a % c


print(power(a, b))
