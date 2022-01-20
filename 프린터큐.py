# deque는 인덱싱이 안됨
from collections import deque

c = int(input())
for _ in range(c):
    count = 0
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))

    while queue:
        # target과 head 미리 저장해놓기
        target = max(queue)
        head = queue.popleft()
        m -= 1

        if target == head:
            count += 1
            if m < 0:
                print(count)
                break
        else:
            queue.append(head)
            if m < 0:
                m = len(queue)-1

