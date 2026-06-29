class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for i, num1 in enumerate(nums):
            # avoid duplicates
            # skip finding other 2 nums for current `i`
            # if it's the identical case to `i-1`
            # *array is sorted: all duplicates are in 1 contiguous chunk
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # enforces a natural sorted requirement to avoid duplicates
            # where `i` will always be the smallest index in the triplet
            # since if we use `left=0` we may find `left,right` st left < i or right < i 
            # which breaks the sorted requirements and encounters duplicates as we have covered <i
            # in previous outer loop iterations
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr = (num2 := nums[left]) + (num3 := nums[right])

                if curr < -num1:
                    left += 1
                elif curr > -num1:
                    right -= 1
                else:
                    out.append((num1, num2, num3))
                    # keep looking, many solutions might add up to `-num1`
                    # look inwards until not duplicate `left,right`
                    # *array is sorted: all duplicates are in 1 contiguous chunk
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
        return out