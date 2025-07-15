class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniquechar = set()
        l = 0
        sublength = 0
        for char in range(len(s)):
            while s[char] in uniquechar:
                uniquechar.remove(s[l]) 
                l += 1
            uniquechar.add(s[char])
            sublength = max(sublength, char-l+1)
        return sublength
            
        