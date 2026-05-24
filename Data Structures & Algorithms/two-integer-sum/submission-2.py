class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for j, num in enumerate(nums):
            if (i := indices.get(target - num)) is not None:
                # i < j is guaranteed as indices is always populated
                # with previously traversed elements as seen below
                return [i, j]
            indices[num] = j