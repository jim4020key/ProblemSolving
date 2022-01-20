n, m = map(int, input().split())
a, b, direction = map(int, input().split())

d = [[0] * m for _ in range(n)] # 방문을 표시하기 위한 배열
d[a][b] = 1 # 현재 좌표 방문 처리
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

game_map = []
for _ in range(n):
    x = list(map(int, input().split()))
    game_map.append(x)


def turn_left():
    global direction
    if direction >= 1:
        direction -= 1
    else:
        direction = 3

count = 0



'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''