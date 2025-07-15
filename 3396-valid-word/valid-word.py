class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        vowels = set("AEIOUaeiou")
        v = False
        c = False
        if len(word) < 3:
            return False
        for w in word:
            if not w.isalnum():
                return False
            if w.isalpha():
                if w in vowels:
                    v = True
                else:
                    c = True
        return v and c


        