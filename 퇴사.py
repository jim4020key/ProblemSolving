# 1) 다이나믹 프로그래밍 2) 브루트포스
n = int(input())
time = []
profit = []
d = []

for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    if i + t-1 < n:
        profit.append(p)
        d.append(p)
    else:   # 상담 끝시간이 퇴사를 넘어가는 경우
        profit.append(0)
        d.append(0)

for i in range(1, n):
    for j in range(0, i):
        if i-j >= time[j]:
            d[i] = max(profit[i] + d[j], d[i])

print(max(d))