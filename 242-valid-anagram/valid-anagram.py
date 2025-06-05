from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        if len(s) != len(t):
            return False
        # hashmap = {}
        # for i in s:
        #     hashmap[i] = hashmap.get(i, 0) + 1
        # for r in t:
        #     if r not in hashmap:
        #         return False
        #     hashmap[r] = hashmap.get(r) - 1
        
        # return not any(hashmap.values())

        scount = [0] * 26
        tcount = [0] * 26

        for c in s:
            scount[ord(c) - ord('a')] += 1
        for c in t:
            tcount[ord(c) - ord('a')] += 1
        return scount == tcount