food_times = list(map(int, input().split()))
k = int(input())

for i in range(k):
    n = 0
    while food_times[(i+n)%len(food_times)] != 0:
        n += 1
    food_times[(i+n)%len(food_times)] -= 1
    answer = (i+n)%len(food_times)

print(answer)