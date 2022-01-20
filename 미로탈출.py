# 반례가 있는지 확인해야 함 ... 책과 다른 풀이
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 9
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0
dfs(0, 0)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 9:
            result += 1

print(result)
