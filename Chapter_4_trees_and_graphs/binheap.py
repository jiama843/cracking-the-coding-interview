import heapq

heap = [1,9,3,7,5,6]
heapq.heapify(heap)
print(heap)

heapq.heappush(heap, 20)
print(heap)

print(heap[0])

heapq.heappop(heap)
print(heap)
