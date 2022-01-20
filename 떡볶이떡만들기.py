'''n, m = map(int, input().split())
array = list(map(int, input().split()))

# 문제에서 절단기의 높이는 최대 10억 => 탐색의 범위가 넓어 수행시간 초과 가능 ...
for i in range(max(array), 0, -1):
    sum = 0
    for j in range(n):
        if array[j] - i >= 0:
            sum += array[j] - i
    if sum >= m:
        result = i
        break

print(result)'''

## 이진탐색 방법!!!!
n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start+end) // 2
    for x in array:
        if x > mid:
            total += x-mid
    if total < m:
        end = mid-1
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답
        start = mid+1

print(result)
