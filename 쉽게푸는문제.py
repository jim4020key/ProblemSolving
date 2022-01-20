array = []
for i in range(1, 100):
    for _ in range(i):
        array.append(i)

a, b = map(int, input().split())
sum = 0
for i in range(a-1, b):
    sum += array[i]

print(sum)