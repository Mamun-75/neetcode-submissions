class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0] * (n + 1)
        for x in range(1, n + 1):
            res[x] = res[x >> 1] + (x & 1)
        return res