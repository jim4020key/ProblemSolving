array = []
for i in range(10000000):
    if '666' in str(i):
        array.append(i)
    if len(array) > 10000:
        break

n = int(input())
print(array[n-1])