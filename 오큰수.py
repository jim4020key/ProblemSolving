import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
stack = []  # 오큰수를 찾지 못한 수의 인덱스
result = [-1 for _ in range(n)]

stack.append(0)
i = 1
while stack and i < n:
    while stack and array[stack[-1]] < array[i]:
        result[stack[-1]] = array[i]
        stack.pop()
    stack.append(i)
    i += 1

print(*result)