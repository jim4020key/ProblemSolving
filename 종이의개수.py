import sys
input = sys.stdin.readline
n = int(input())
array = []
result = []
for _ in range(n):
    array.append(list(map(int, input().split())))

def divide_paper(x, y, n):
    global result
    color = array[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != array[i][j]:
                result.append('(')
                divide_paper(x, y, n // 3)
                divide_paper(x, y + n // 3, n // 3)
                divide_paper(x, y + n // 3 * 2, n // 3)

                divide_paper(x + n // 3, y, n // 3)
                divide_paper(x + n // 3, y + n // 3, n // 3)
                divide_paper(x + n // 3, y + n // 3 * 2, n // 3)

                divide_paper(x + n // 3 * 2, y, n // 3)
                divide_paper(x + n // 3 * 2, y + n // 3, n // 3)
                divide_paper(x + n // 3 * 2, y + n // 3 * 2, n // 3)
                result.append(')')
                return
    result.append(color)

divide_paper(0, 0, n)
negative_cnt = result.count(-1)
zero_cnt = result.count(0)
positive_cnt = result.count(1)

print(negative_cnt)
print(zero_cnt)
print(positive_cnt)