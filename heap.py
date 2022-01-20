import heapq

def minheapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def maxheapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

minresult = minheapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
maxresult = maxheapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(minresult)
print(maxresult)