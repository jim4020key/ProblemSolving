n, k = map(int, input().split())
array = [i+1 for i in range(n)]
result = []
i = 0
while array:
    temp = (i+k-1)%len(array)
    result.append(array.pop(temp))
    i = temp

print('<', end='')
for i in range(n-1):
    print(result[i], end=', ')

print(result[n-1], end='>')