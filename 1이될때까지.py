# n이 1이 되는 최소 횟수
# n에서 1을 빼거나 n을 k로 나누거나
n, k = map(int, input().split())
count = 0
'''
while True:
    if n == 1:
        break
    if n%k == 0:
        n = n / k
        count += 1
    else:
        n -= 1
        count += 1
        
print(count)
'''

# 최대한 많이 나누기
while True:
    # 나누어 떨어질 때까지 1씩 빼기
    target = (n//k) * k
    count += (n-target)
    n = target
    if n < k:   # 더 이상 나눌 수 없을 때
        break
    count += 1
    n //= k

count += (n-1)  # n을 0으로 만들었기 때문
print(count)