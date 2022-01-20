n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
price_t = price[0]
for i in range(n-1):
    if price[i] < price_t:
        price_t = price[i]
    result += price_t * dist[i]

print(result)