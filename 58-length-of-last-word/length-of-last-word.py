class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        last = len(s) -1
        while s[last] == " " and last >= 0:
            last -= 1
        
        while s[last] != " " and  last >= 0:
            count += 1
            last -= 1
        
        return count
        