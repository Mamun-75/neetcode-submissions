class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        current = 0
        for n in nums:
            if current<0:
                current = 0
            current +=n
            best = max(best, current)
        return best
        