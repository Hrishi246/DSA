import heapq

#It will be minimum heap implementation in python
heap = [4, 7, 3, -2, 1, 0]
num = [4, 7, 3, -2, 1, 0]
heap_data = []
# print(heap)
heapq.heapify(heap)
# print(heap)

for value in num:
    heapq.heappush(heap_data, value)

# print(heap_data)

while heap_data:
    print(heapq.heappop(heap_data))