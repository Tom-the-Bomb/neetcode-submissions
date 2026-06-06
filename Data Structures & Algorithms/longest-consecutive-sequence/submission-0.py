class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)

        nums = set(nums)
        ans = 0

        for num in nums:
            if num - 1 not in nums:
                num += 1
                curr = 1
                while num in nums:
                    curr += 1
                    num += 1
                ans = max(ans, curr)
        return ans