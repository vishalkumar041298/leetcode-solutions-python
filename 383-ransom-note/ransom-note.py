class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mc = defaultdict(int)

        for c in magazine:
            mc[c] += 1
        
        for c in ransomNote:
            if c not in mc:
                return False
            mc[c] -= 1
            if mc[c] == 0:
                del mc[c]
        return True