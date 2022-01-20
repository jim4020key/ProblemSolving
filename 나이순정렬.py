n = int(input())
array = []
for _ in range(n):
    age, name = map(str, input().split())
    array.append([int(age), name])

array.sort(key = lambda x: x[0])

for i in range(n):
    print(array[i][0], array[i][1])