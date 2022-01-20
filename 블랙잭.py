# 브루트포스를 가능하게 하는 조건?
n, m = map(int, input().split())
array = list(map(int, input().split()))

result = []
breaker = False
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if array[i]+array[j]+array[k] <= m:
                result.append(array[i]+array[j]+array[k])


print(max(result))