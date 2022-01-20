# greedy algorithm
s = input()
s += "2"    # 문자열의 마지막에 0, 1이 아닌 숫자를 붙여서 비교

# 연속된 1의 개수와 0의 개수
zero = 0
one = 0

for i in range(len(s)-1):
    if int(s[i]) == 0 and int(s[i+1]) != 0:
        zero += 1
    if int(s[i]) == 1 and int(s[i + 1]) != 1:
        one += 1

count = min(zero, one)


print(count)