class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for index in range(n+1):
            x = index
            count = 0
            while x!=0:
                if (x&1)== 1:
                    count+=1
                x = x>>1
            res.append(count)
        return res