n = int(input())
count =0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # str으로 변경 후 concat -> '3'이 포함되어 있는지 확인하는 방법 ...
            """if '3' in str(i) + str(j) + str(k):
                count += 1"""
            if k % 10 == 3:
                count += 1
            elif (k//10) % 10 == 3:
                count += 1
            elif j % 10 == 3:
                count += 1
            elif (j//10) % 10 == 3:
                count += 1
            elif i % 10 == 3:
                count += 1
print(count)