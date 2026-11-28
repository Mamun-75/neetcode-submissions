class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        best = nums[0]

        for n in nums[1:]:
            current = max(current+n, n)
            best = max(current, best)
        return best
## this is kadane's algorithm version