# s는 서로 다른 n개의 자연수의 합, n의 최대는?
s = int(input())
count = 0
a = 1
while True:
    s -= a
    a += 1
    count += 1
    if s < a:
        break

print(count)