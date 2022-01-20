# 선발할 수 있는 신입사원의 최대 인원수
# input이 많은 경우 시간 초과
# => sys.stdin.readline().rstrip()
# +)동석차가 존재하지 않기 때문에 각 인덱스를 서류 성적 순위로, 인덱스의 값을 면접 성적 순위로 설정하고 풀면 이중 배열 사용 불필요
import sys

t = int(input())
result = []
for _ in range(t):
    rank = []
    n = int(input())
    for _ in range(n):
        l = list(map(int, sys.stdin.readline().rstrip().split()))
        rank.append(l)
    rank.sort(key=lambda x: x[0])
    count = len(rank)
    # 서류 등수 기준 바로 앞 사람의 면접 등수만 확인해도 되는가?
    # min_rank !!
    min_rank = rank[0][1]
    for i in range(len(rank)):
        if rank[i][1] > min_rank:
            count -= 1
        if rank[i][1] < min_rank:
            min_rank = rank[i][1]
    result.append(count)

for i in range(len(result)):
    print(result[i])
