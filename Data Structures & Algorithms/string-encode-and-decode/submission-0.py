class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" # this is the variable where we aim to store the encoded string,
        """
        our plan is to count length of each string from input list, and put the
        number first , then use a pound sign so we can mark the starting of a new
        string when decoding , then add the string : for example: ["leet","code"]
        will be "4#leet4#code"


        and while decoding  we will find # , and the length of the string will be
        the previous character or charecters, that is int(s[i:j]) where j is the position of that # character and i is the starting position of the string like 0, then we find string by adding length of the string with the j+1 position, and append it to the result list, we need to update i with i += j+1+length 

        """ 
        for s in strs: 
            res += str(len(s))+'#'+s
        return res


    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j+1 + length
        return res


