n, k = map(int, input().split())
array = [True for i in range(n + 1)]

for i in range(2, n+1):
    if array[i]:
        k -= 1
        if k == 0:
            print(i)
            break
        j = 2
        while i * j <= n:
            if array[i * j]:
                k -= 1
            if k == 0:
                print(i*j)
                break
            array[i * j] = False
            j += 1

