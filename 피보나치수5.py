# 짝수 번째 항, 홀수 번째 항의 특성
n = int(input())
array = [0] * (n+1)
if n > 0:
    array[1] = 1

def fibo(n):
    if n <= 1:
        return array[n]
    else:
        if n % 2 == 1:
            m = (n+1) // 2
            t1 = fibo(m)
            t2 = fibo(m-1)
            array[n] = t1*t1 + t2*t2
        else:
            m = n // 2
            t1 = fibo(m-1)
            t2 = fibo(m)
            array[n] = 2*t1*t2 + t2*t2
        return array[n]

print(fibo(n))
