# 최소 치킨 거리 구하기

n, m = map(int, input().split())
loc = []
for _ in range(n):
    input_list = list(map(int, input().split()))
    loc.append(input_list)
chicken_dist = 0

house = []
chicken_store = []
for i in range(n):
    for j in range(n):
        if loc[i][j] == 1:
            house.append([i, j])
        if loc[i][j] == 2:
            chicken_store.append([i, j])

# 폐점해야 하는 치킨집을 결정하는 방법?
# 모든 집으로의 거리 합이 가장 작은 순서대로 m개만 남기는 방법
### 거리의 합이 같은 치킨집이 존재한다면?
### 치킨집 개수는 m보다 작을 수 있다 ==> 완전탐색 (combinations)
if len(chicken_store) > m:
    for x in chicken_store:
        dist_sum = 0
        for y in house:
            dist_sum += abs(x[0] - y[0]) + abs(x[1] - y[1])
        x.append(dist_sum)
    chicken_store.sort(key = lambda k: k[2])

# print(chicken_store)
for x in house:
    min_dist = 1000
    for y in chicken_store[:m]:
        if abs(x[0]-y[0]) + abs(x[1]-y[1]) < min_dist:
            min_dist = abs(x[0]-y[0]) + abs(x[1]-y[1])
    chicken_dist += min_dist

print(chicken_dist)
