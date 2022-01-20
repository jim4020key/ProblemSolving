# 피사노주기
n = int(input())
n %= 15*(10**5)

array = [0] * (n+1)
array[1] = 1

for i in range(2, n+1):
    array[i] = array[i-1] + array[i-2]
    array[i] %= 1000000     # 메모리 초과 때문에 추가

print(array[n])