# n개의 보석, 각 보석의 무게와 가격(m,v), k개의 가방, 가방의 수용가능무게 c
# 훔칠 수 있는 보석의 최대 가격?
n, k = map(int, input().split())
gem = []
bag = []
for _ in range(n):
    x = list(map(int, input().split()))
    gem.append(x)
for _ in range(k):
    c = int(input())
    bag.append(c)

# 훔칠 수 있는 보석의 최대 무게와 다른 문제
# 같은 보석을 두 가방에 담을 수 없다 ... remove?
# ... 내림차순 정렬 후 넣을 수 있는 최소 무게의 가방에 넣는다?
# => queue를 써야 하는가?

gem.sort(key=lambda x :x[0])
bag.sort()
max_w = 0
max_sum = 0
# 가능한 weight 중에서 max_value
# => 2중 for문으로 시간 초과
for i in range(len(bag)):
    for j in range(len(gem)):
        print(bag[i])
        if gem[j][0] <= bag[i]:
            max_w = gem[j][1]
    max_sum += max_w

print(max_sum)