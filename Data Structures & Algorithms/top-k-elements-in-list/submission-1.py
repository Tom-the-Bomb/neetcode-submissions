from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        heap = []
        for i, (num, count) in enumerate(counter.items()):
            # push all into max heap
            heappush(heap, (-count, num))
            
        out = []
        for i in range(k):
            # pop k most frequent (largest val) elements
            out.append(heappop(heap)[1])
        return out