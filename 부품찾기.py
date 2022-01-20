# 방법1 ... 집합자료형
'''
n = int(input())
items = input().split()
m = int(input())
array = input().split()

for i in array:
    if i in items:
        print("yes", end=' ')
    else:
        print("no", end=' ')
'''

# 방법2 ... 이진탐색
'''
n = int(input())
items = list(map(int, input().split()))
items.sort() # 이진탐색을 위해서는 사전에 정렬 필요 !!!!!!!!!
m = int(input())
array = list(map(int, input().split()))


def recursive_binary_search(array, target, start, end):
    if start > end:
        print("no", end=' ')
        return False
    mid = (start+end) // 2
    if array[mid] == target:
        print("yes", end=' ')
        return True
    elif array[mid] > target:
        return recursive_binary_search(array, target, start, mid-1)
    else:
        return recursive_binary_search(array, target, mid+1, end)

for i in array:
    recursive_binary_search(items, i, 0, n-1)
'''


# 방법3 ... 계수정렬
n = int(input())
items = list(map(int, input().split()))
m = int(input())
array = list(map(int, input().split()))

# 모든 원소의 번호를 포함할 수 있는 크기의 리스트 생성
# -> max(items)+1로 설정시 index out of range
count = [0] * 1000001

for i in range(len(items)):
    count[items[i]] = 1

for i in array:
    if count[i] == 1:
        print("yes", end=" ")
    else:
        print("no", end=' ')
