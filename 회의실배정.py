# 회의실을 사용할 수 있는 회의의 최대 개수
n = int(input())
time = []
count = 0
for i in range(n):
    x = list(map(int, input().split()))
    time.append(x)
time.sort(key=lambda k: (k[1], k[0]))
# 종료시간을 기준으로 정렬
# => [1,4], [8,8], [4,8]의 경우 오류 발생 ... 시작시간과 종료시간이 같은 경우
# => 다중 조건

start = 0
for i in range(len(time)):
    if time[i][0] >= start:
        count += 1
        start = time[i][1]

print(count)
