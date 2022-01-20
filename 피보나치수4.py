# 행렬
import sys
ZERO = [[1, 0], [0, 1]]     # 행렬의 항등원


def multiply(mat1, mat2):     # 행렬의 곱셈
    ans = []
    for i in range(len(mat1)):
        ans.append([])
        for j in range(len(mat2[0])):
            temp = 0
            for k in range(len(mat1[0])):
                temp += mat1[i][k] * mat2[k][j]
            ans[i].append(temp)
    return ans


def power(mat, p):   # 행렬의 거듭제곱
    if p == 0:
        return ZERO
    if p == 1:
        return mat
    else:   # 분할 정복을 이용한 거듭제곱
        temp = power(mat, p // 2)
        if p % 2 == 0:
            return multiply(temp, temp)
        else:
            return multiply(multiply(temp, temp), mat)


n = int(sys.stdin.readline())
m = [[1, 1], [1, 0]]
print(power(m, n)[0][1])    # print(power(m, n)[1][0])