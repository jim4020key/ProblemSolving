n, k = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

count = 0
for i in range(n-1, -1, -1):
    count += k // array[i]
    k = k % array[i]

print(count)