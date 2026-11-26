class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1  +  nums2
        nums.sort()
        l = 0
        r = len(nums) - 1
        mid = (l+r)//2
        if (len(nums))%2 == 0:
            return (nums[mid] + nums[mid+1])/2
        else:
            return nums[mid]
