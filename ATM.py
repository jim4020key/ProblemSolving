# 돈을 인출하는데 필요한 시간의 합의 최솟값
n = int(input())
time = list(map(int, input().split()))

# 순서의 가능한 형태 n!
# n!경우를 모두 계산?
# => 시간이 적게 걸리는 사람을 앞으로 ... 정렬
# 각각의 원소를 (list의 length - index)번 더함
time.sort()
result = 0
for i in range(len(time)):
    result += (len(time)-i) * time[i]

print(result)
