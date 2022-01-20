n = int(input())
coins = list(map(int, input().split()))
coins.sort()

#만들 수 없는 최솟값
result = 1
for i in coins:
    if result < i:
        break
    else:
        result += i

print(result)