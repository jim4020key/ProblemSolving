# 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력
def hansoo(num):
    if num < 100:
        return True
    else:
        diff = (num%100)//10 - num%10
        num //= 10
        while num >= 10:
            if (num%100)//10 - num%10 != diff:
                return False
            num //= 10
        return True


n = int(input())
count = 0
for i in range(1, n+1):
    if hansoo(i):
        count += 1

print(count)