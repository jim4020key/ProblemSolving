# 쿼드트리: 트리의 자식노드가 4개인 트리 => 재귀
import sys
input = sys.stdin.readline
n = int(input())
array = []
result = []
for _ in range(n):
    array.append(list(map(int, input().split())))

def quad_tree(x, y, n):
    global result
    color = array[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != array[i][j]:
                result.append('(')
                quad_tree(x, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                result.append(')')
                return
    result.append(color)

quad_tree(0, 0, n)
white_cnt = result.count(0)
blue_cnt = result.count(1)

print(white_cnt)
print(blue_cnt)