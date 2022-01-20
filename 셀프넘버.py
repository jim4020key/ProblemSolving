# 셀프넘버: 생성자가 없는 숫자
# 생성자: 주어진 숫자를 (n + n의 각자리 숫자의 합)이라고 할 때 n
## set 사용히기 ******
num = [False for _ in range(10001)]


def d(n):
    result = n
    while True:
        if n == 0:
            break
        result += (n % 10)
        n //= 10
    return result

for i in range(1, 10001):
    idx = d(i)
    if idx <= 10000:
        num[idx] = True # 셀프 넘버가 아니면 True

for i in range(1, 10001):
    if not num[i]:
        print(i)

