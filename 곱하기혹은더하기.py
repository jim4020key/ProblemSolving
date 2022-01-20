# greedy algorithm
s = input()
result = 1
for i in s:
    if int(i) != 0:
        result *= int(i)
    else:
        result += int(i)



print(result)