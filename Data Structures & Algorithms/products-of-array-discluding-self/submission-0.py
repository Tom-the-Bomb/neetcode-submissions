from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefixes = [1]
        for i, num in enumerate(nums):
            if i == n - 1:
                break
            prefixes.append(num * prefixes[i])
        
        suffixes = [1]
        for i, num in enumerate(reversed(nums)):
            if i == n - 1:
                break
            suffixes.append(num * suffixes[i])

        return [a * b for a, b in zip(prefixes, reversed(suffixes))]