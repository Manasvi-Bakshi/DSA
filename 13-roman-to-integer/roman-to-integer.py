class Solution:
    def romanToInt(self, s: str) -> int:
        RomanSymbol = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        answer,i = 0,0
        while i < len(s):
            if i+1 < len(s) and RomanSymbol[s[i]] < RomanSymbol[s[i+1]]:
                answer += RomanSymbol[s[i+1]] - RomanSymbol[s[i]]
                i += 2
            else:
                answer += RomanSymbol[s[i]]
                i += 1
        return answer
        