import heapq

arr = [1,2,3,9,10,12]

heapq.heapify(arr)

print(arr)

a = heapq.heappop(arr)
print(a)
print(arr)