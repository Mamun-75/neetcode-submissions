class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxn = 0
        for x in nums:
            if x == 1:
                count += 1
                if count> maxn:
                    maxn = count
            else:
                count = 0

        return maxn

            

