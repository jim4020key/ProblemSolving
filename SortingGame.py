# 너비 우선 탐색
# 뒤집기 연산을 이용한 정렬
# 배열의 길이가 1<=n<=8
import sys
from collections import deque


def bfs(start, length):
    queue = deque()
    queue.append((start, 0))
    dp['12345678'] = 0

    while queue:
        now, level = queue.popleft()

        for i in range(len(now)):
            for j in range(i+1, len(now)):
                now[i:j+1] = now[i:j+1][::-1]       # [::-1] 역순으로
                string = "".join(now)

                if dp.get(string) is None:
                    queue.append((list(now), level+1))
                    dp[string] = level+1

                now[i:j+1] = now[i:j+1][::-1]


T = int(sys.stdin.readline().rstrip())
dp = {}     # dictionary

array = [str(num+1) for num in range(8)]
bfs(array, len(array))

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))

    sorted_arr = list(sorted(array))
    mapped = dict(zip(sorted_arr, range(1, N+1)))

    array = [mapped[num] for num in array]
    array = array + [num+1 for num in range(len(array), 8)]
    key = "".join(map(str, array))
    print(dp[key])
