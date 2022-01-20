# 완전탐색 -> 시간초과
n = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(n-1)//2])