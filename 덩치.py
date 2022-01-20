import sys
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

rank = [0]*n
# N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해진다.
for i in range(n):
    k = 0
    for j in range(n):
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            k += 1
    rank[i] = k + 1

for i in range(n):
    print(rank[i], end=' ')
