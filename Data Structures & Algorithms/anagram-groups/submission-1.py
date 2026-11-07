from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """ THIS IS SORTED METHOD 
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())

        """
        # This is optimal method
        groups = defaultdict(list)
        for s in strs:
            count = [0]*26
            
            for ch in s:
               count[ord(ch) - ord('a')]+=1
            
            key = tuple(count)

            groups[key].append(s)
        
        return list(groups.values())

    