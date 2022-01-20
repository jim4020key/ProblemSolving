"""
1, 2, 3 ... 을 계속 더해 나갈 때,
그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
계속 더하는 프로그램을 작성해보자.

즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.

n = int(input())
sum = 0
i = 1

while n > sum:
    sum += i
    i += 1

print(i-1)
"""
"""
## 16진법 구구단
n = int(input(), 16)
for i in range(1, 16):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep ='')
"""
"""
###1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,
###3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다.
###33과 같이 3,6,9가 두 번 들어간 수 일때, "짝짝"과 같이 박수를 두 번 치는 형태도 있다. => str.count()

n = int(input())
for i in range(1, n+1):
    if i%10 == 3 or i%10 == 6 or i%10 == 9:
        print("X", end =" ")
    else:
        print(i, end=" ")
"""
"""
a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)

for i in range(1, n):
    a = a * m + d

print(a)
"""
"""
d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input())
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1
for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=" ")
    print()
"""
"""
### 십자 뒤집기
d=[]
for i in range(20): ## list 생성 후 모두 0을 채워 넣음
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(19): ## 입력을 첫 줄 부터 차례로 list에 저장
    a = input().split()
    for j in range(19):
        d[i+1][j+1] = int(a[j])

n = int(input()) ## 십자 뒤집기 횟수
for i in range(n):
    x,y=input().split()
    x=int(x)
    y=int(y)
    for j in range(1, 20): ## 가로줄 뒤집기
        if d[j][y]==0:
            d[j][y]=1
        else:
            d[j][y]=0
        if d[x][j]==0: ## 세로줄 뒤집기
            d[x][j]=1
        else:
            d[x][j]=0
for i in range(1, 20): ## 변경된 바둑판 출력
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()
"""
"""
### 설탕과자 놓기
h,w = input().split()
h = int(h)
w = int(w)
m = []
for i in range(h+1):
    m.append([])
    for j in range(w+1):
        m[i].append(0)
n = int(input())
for i in range(n):
    l,d,x,y = input().split()
    if int(d)==0:
        for j in range(int(l)):
            m[int(x)][int(y)+j] = 1
    else:
        for j in range(int(l)):
            m[int(x)+j][int(y)] = 1
for i in range(1, h+1):
    for j in range(1, w+1):
        print(m[i][j], end=' ')
    print()
"""

### 성실한 개미
m = []
for i in range(12): ## 리스트 생성
    m.append([])
    for j in range(12):
        m[i].append(0)
for i in range(10): ## input 저장
    a = input().split()
    for j in range(10):
        m[i+1][j+1] = int(a[j])
x = 2 ## 출발점(2,2)
y = 2
while True:
    if m[x][y] == 0: ## 벽이 아니면 이동 가능
        m[x][y] = 9 ## 경로에 9를 출력
    elif m[x][y] == 2:
        m[x][y] = 9
        break ## 목적지에 도착하면 종료
    if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9): ## 더이상 움직일 수 없을 때 종료
        break
    if m[x][y+1] != 1: ## 오른쪽에 길이 있으면 오른쪽으로 이동
        y += 1
    elif m[x+1][y] != 1: ## 오른쪽에 길이 없고 아래에 길이 있으면 아래로 이동
        x += 1
for i in range(1, 11): ## 결과 출력
    for j in range(1, 11):
        print(m[i][j], end=' ')
    print()

