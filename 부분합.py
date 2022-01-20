n, s = map(int, input().split())
array = list(map(int, input().split()))

len_array = []
interval_sum = 0
end = 0
len = 0

for start in range(n):
    while interval_sum < s and end < n:
        interval_sum += array[end]
        len += 1
        end += 1
    if interval_sum >= s:
        len_array.append(len)
    interval_sum -= array[start]
    len -= 1

if len_array:
    print(min(len_array))
else:
    print(0)