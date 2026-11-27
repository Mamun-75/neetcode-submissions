class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = (n*(n+1))//2
        a = sum(nums)
        return total - a