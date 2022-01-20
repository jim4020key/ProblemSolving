# 피보나치 함수
# 재귀함수

'''def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-2) + fibo(x-1)

print(fibo(4))'''

# 메모이제이션(탑다운) ... 재귀적
'''d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))'''

# DP테이블(바텀업)
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])