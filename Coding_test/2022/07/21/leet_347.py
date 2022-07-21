import collections
import heapq


def topKFrequent(nums, k):
    # c = collections.Counter(nums)
    # c_heap = []
    # for i in c:
    #     heapq.heappush(c_heap,  (-c[i], i))
    #
    # topk = list()
    # for _ in range(k):
    #     topk.append(heapq.heappop(c_heap)[1])
    # return topk
    return list(list(zip(*collections.Counter(nums).most_common(k)))[0])

print(topKFrequent([1, 1, 1, 2, 2, 3], 2))

a = [1, 2, 3, 4]
b = ["a", "b", "c", "d"]
c = ["!", "@", "#"]

print(list(zip(a, b, c)))