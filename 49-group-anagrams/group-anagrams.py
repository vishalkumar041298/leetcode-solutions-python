from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            
            key = tuple(count)
            hashmap[key].append(s)
        return list(hashmap.values())