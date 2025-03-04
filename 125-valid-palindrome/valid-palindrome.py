import re 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        
        s =re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        r = len(s) - 1
        print(s)
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True