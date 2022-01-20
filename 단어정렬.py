n = int(input())
array = []
for _ in range(n):
    array.append(input())
array = list(set(array))    # 중복제거

array.sort(key = lambda x: (len(x), x))

result = '\n'.join(array)
print(result)