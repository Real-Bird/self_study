import heapq

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(heap, (abs(x), x))
    else:
        if not heap:
            print(0)
        else:
            tmp1, tmp2 = heapq.heappop(heap)
            print(tmp2)