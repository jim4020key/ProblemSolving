import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
target = list(map(int, input().split()))
queue = deque([i for i in range(1, n+1)])
count = 0

while target:
    if queue.index(target[0]) < len(queue)-queue.index(target[0]):
        while True:
            if queue[0] == target[0]:
                del queue[0]
                del target[0]
                break
            else:
                queue.append(queue[0])
                del queue[0]
                count += 1

    else:
        while True:
            if queue[0] == target[0]:
                del queue[0]
                del target[0]
                break
            else:
                queue.insert(0, queue[-1])
                del queue[-1]
                count += 1

print(count)