class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
        n = len(s)
        lps = [0] * len(s)

        prevlps = 0
        i = 1
        while i < len(s):
            if s[i] == s[prevlps]:
                lps[i] = prevlps + 1
                prevlps += 1
                i += 1
            elif prevlps == 0:
                i += 1
            else:
                prevlps = lps[prevlps - 1]
        
        lps = lps[-1]

        return lps>0 and n % (n-lps) == 0
