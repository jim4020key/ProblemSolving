k = int(input())
money = []

for _ in range(k):
    n = int(input())
    if n == 0:
        del money[-1]
    else:
        money.append(n)


print(sum(money))