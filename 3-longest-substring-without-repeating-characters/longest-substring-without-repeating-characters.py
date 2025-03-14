class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = set()
        maxsub = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            maxsub = max(maxsub, len(char_set))
        return maxsub
            
