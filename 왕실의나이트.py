# 8*8 체스판에서 움직일 수 있는 경우의 수
# 입력은 a~h+1~8의 형태

loc = input()
x = ord(loc[0]) - ord('a') + 1
y = int(loc[1])
count = 0

'''if x + 2 <= 8:
    if y + 1 <= 8:
        count += 1
    if y - 1 >= 1:
        count += 1

if x - 2 >= 1:
    if y + 1 <= 8:
        count += 1
    if y - 1 >= 1:
        count += 1

if y + 2 <= 8:
    if x + 1 <= 8:
        count += 1
    if x - 1 >= 1:
        count += 1

if y - 2 >= 1:
    if x + 1 <= 8:
        count += 1
    if x - 1 >= 1:
        count += 1'''

# 나이트가 갈 수 있는 모든 step을 정의 ... step이 체스판을 넘어가는지를 검사하는 방법
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]
    if 1 <= next_x <= 8 and 1 <= next_y <= 8:
        count += 1

print(count)