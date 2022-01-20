n, m = map(int, input().split())
'''2차원배열 불필요
l = []
for i in range(n):
    l.append([])
    for j in range(m):
        l[i].append(0)
for i in range(n):
    a = input().split()
    for j in range(m):
        l[i][j] = int(a[j])

result = 0
pick = min(l[0])
for i in range(n):
    if pick <= min(l[i]):
        result = min(l[i])
'''

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)