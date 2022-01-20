# 재귀
n = int(input())
array = [-1] * (n+1)

def fibo(n):
    if n < 2:
        return n
    if array[n] != -1:
        return array[n]
    array[n] = fibo(n - 1) + fibo(n - 2)
    return array[n]


print(fibo(n))