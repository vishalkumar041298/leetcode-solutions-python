from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False

        hashmap = {}

        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        
        for c in t:
            hashmap[c] = hashmap.get(c, 0) - 1
        
        return not any(hashmap.values)