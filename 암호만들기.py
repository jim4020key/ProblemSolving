# 중복 X, 증가하는 순서로 배열 => 조합
# 최소 한 개의 모음과 최소 두 개의 자음
from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
l, c = map(int, input().split())
array = input().split(' ')
array.sort()

for password in combinations(array, l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    if 1 <= count <= l - 2:
        print(''.join(password))
