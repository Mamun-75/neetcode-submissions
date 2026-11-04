class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j]==target:
                     return [i,j]

            this brute force solution is ok, but O(n^2), 
        """
        seen = {}
        for i , num in enumerate(nums):
            complement  = target - num
            if complement in seen:
                return [seen[complement], i]

            seen[num]=i
        return []
        

    ## now time complexity is O(n), though space complexity is O(n) where previously O(1), its kind of a trade off
        