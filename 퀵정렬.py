array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

'''
def quick_sort(array, start, end):
    if start >= end: # list의 원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
'''


# 파이썬의 장점을 살린 퀵정렬 소스

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]
    # 피봇과 데이터를 비교하는 비교 연산 횟수가 증가
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))