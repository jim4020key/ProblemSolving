from collections import deque
# FIFO

n = int(input())
array = deque([])
for i in range(1, n+1):
    array.append(i)

while len(array) > 1:
    array.popleft()
    temp = array.popleft()
    array.append(temp)

print(array[0])