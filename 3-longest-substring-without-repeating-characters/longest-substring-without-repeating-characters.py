class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        res = 0

        for r in range(n+1):
            substr = s[l:r]
            if len(substr) == len(set(substr)):
                res = max(len(substr), res)
            else:
                l = l + 1

        return res
            
