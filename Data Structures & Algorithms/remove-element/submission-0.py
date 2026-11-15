class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        k = 0
        for i in range(len(nums)):
            if nums[i]!= val:
                nums[k]=nums[i]
                k+=1
        return k 
        """
        #another better solution from two pointer:
        i = 0
        n = len(nums)
        while i<n:
            if nums[i]==val:
                n-=1
                nums[i]=nums[n]
            else:
                i+=1
        return n
                

        
        