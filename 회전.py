# a: n의 각 자리숫자의 합, b: n의 각 자리수를 1로 만든 숫자
# 모든 n에 대하여 답은 a*b
origin = input()
sum = 0
rotate = int(origin)
for _ in range(len(origin)):
    temp = rotate // 10 + (rotate % 10 * 10**(len(origin)-1))
    sum += temp
    rotate = temp

print(sum)