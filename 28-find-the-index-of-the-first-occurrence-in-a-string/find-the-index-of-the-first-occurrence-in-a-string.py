class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        lps = [0] * m
        prevlps = 0
        i = 1

        while i < m:
            print(i)
            if needle[prevlps] == needle[i]:
                lps[i] = prevlps + 1
                prevlps += 1
                i+=1
            elif prevlps == 0:
                lps[i] = 0
                i+=1
            else:
                prevlps = lps[prevlps-1]
        
        i = 0
        j = 0
        print(lps)
        while i < n:
            if needle[j] == haystack[i]:
                i, j = i+1, j+1
                if j == m:
                    return i - m
            elif j == 0:
                i += 1
            else:
                j = lps[j-1]
        
        
        return -1
