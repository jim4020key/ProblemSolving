n = int(input())
array = []
for _ in range(n):
    array.append(input().split())
# 입력을 튜플로 받는 방법
'''for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))'''


array.sort(key=lambda x: int(x[1]))

for i in array:
    print(i[0], end = ' ')