# 벽 3개 ... 조합
# Python3 시간초과
import copy
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
virus_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus_list.append([i, j])
temp = [[0]*m for _ in range(n)]    # 벽을 설치한 후

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
def spread_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 바이러스가 퍼질 수 있으면
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                spread_virus(nx, ny)

# 벽 설치(dfs)
def dfs(count):
    global result
    global temp
    if count == 3:
        temp = copy.deepcopy(graph)
        for virus in virus_list:
            spread_virus(virus[0], virus[1])
        score = sum(i.count(0) for i in temp)
        result = max(result, score)
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)