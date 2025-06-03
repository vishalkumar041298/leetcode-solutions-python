from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) + 1
        for r in t:
            if r not in hashmap:
                return False
            hashmap[r] = hashmap.get(r) - 1
        
        return not any(hashmap.values())