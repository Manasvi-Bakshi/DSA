class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for letter in range(len(strs[0])):    
            for word in strs:
                if letter == len(word) or word[letter] != strs[0][letter]:
                    return res
            res += strs[0][letter]
        
        return res
            
        