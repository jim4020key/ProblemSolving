# n을 3kg, 5kg으로 나누는 최소 봉지 개수
n = int(input())
a = b = 10000
c = 0

# 3의 개수가 5의 개수와 같거나 큰 경우
# 3으로 나누어 질 때 까지 5를 하나씩 빼보자 ... 반례 존재
# => 3을 하나씩 빼야 하는 이유?

# 4가지 경우가 모두 필요한가?
# a가 불필요해 보임 ... 결정에 영향X ... b나 c랑 같은 결과

"""if (n%5) % 3 == 0:
    a = n // 5 + (n%5) // 3"""

if n % 5 == 0:
    a = n // 5
if n % 3 == 0:
    b = n // 3
while n > 3:
    n -= 3
    c += 1
    if n % 5 == 0:
        c += n // 5
        n = 0
        break
if n != 0:
    c = 10000

if a == b == c:
    print(-1)
else:
    print(min(a, b, c))
