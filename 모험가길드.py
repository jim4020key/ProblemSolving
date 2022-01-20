# greedy algorithm
n = int(input())
array = list(map(int, input().split()))
count = 0

array.sort(reverse=True)

k = 0
while k < len(array):
    if array[k] <= len(array)-k:
        k += array[k]
        count += 1


print(count)