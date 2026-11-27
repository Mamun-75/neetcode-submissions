class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        for i , n in enumerate(nums):
            res  = res^i^n
        return res