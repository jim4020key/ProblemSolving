# 다시 칠해야 하는 정사각형의 최소 개수
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(input())

count = []
for a in range(n-7):
    for b in range(m-7):
        count_w = 0     # 체스판이 W로 시작하는 경우
        count_b = 0     # 체스판이 B로 시작하는 경우
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:
                    if array[i][j] != 'W': count_w += 1
                    if array[i][j] != 'B': count_b += 1
                else:
                    if array[i][j] != 'B': count_w += 1
                    if array[i][j] != 'W': count_b += 1
        count.append(min(count_w, count_b))

print(min(count))


