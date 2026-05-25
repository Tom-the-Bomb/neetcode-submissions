from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        heap = []
        for i, (num, count) in enumerate(counter.items()):
            heappush(heap, (count, num))
            if len(heap) > k:
                # pop once to remove rarest element
                heappop(heap)
            
        return [n for _, n in heap]