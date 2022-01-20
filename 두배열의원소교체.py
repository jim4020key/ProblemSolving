n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


# 최대 k번 => b가 더 클때만 바꾸기 ... 앞에서부터 k개를 모두 바꾸면 XXX
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))