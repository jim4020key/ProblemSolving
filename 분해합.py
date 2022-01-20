# n의 가장 작은 생성자
n = int(input())
array = []
for i in range(n):
    temp = i
    result = temp % 10
    temp //= 10
    while temp >= 10:
        result += temp % 10
        temp //= 10
    if result+temp+i == n:
        array.append(i)

if array:
    print(min(array))
else:
    print(0)