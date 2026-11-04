class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        return Counter(s) == Counter(t)
        this is a solution in one line 
        
        """ 
        """
            return sorted(s)==sorted(t)
            this is another solution , with O(nlogn)

        """
        
        ## the below approach is better O(n+m)
        
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}

        for ch in s:
            count_s[ch] = count_s.get(ch,0)+1
        
        for ch in t:
            count_t[ch] = count_t.get(ch,0)+1

        return count_s == count_t



        