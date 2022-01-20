# 얼음을 얼릴 수 있는 곳 0, 막힌 곳 1
# 아이스크림의 갯수는??
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
