class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        currentsum = sum(arr[:k])
        count = 0
        if currentsum/k >=threshold:
            count+=1
            
        for i in range(k, len(arr)):
            currentsum = currentsum + arr[i] - arr[i-k]
            if currentsum/k >=threshold:
                count+=1
        return count   