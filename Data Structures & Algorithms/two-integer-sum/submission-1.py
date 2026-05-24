class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {n: i for i, n in enumerate(nums)}

        for i, num in enumerate(nums):
            if (j := indices.get(target - num)) and i != j:
                return sorted((i, j))