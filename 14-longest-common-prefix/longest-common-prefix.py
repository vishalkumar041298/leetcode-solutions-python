class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0

        while i < len(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1
        return strs[0]

        
