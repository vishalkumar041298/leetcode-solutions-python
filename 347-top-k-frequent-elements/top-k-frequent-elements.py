class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        freqs = [[] for _ in range(len(nums)+1)]

        for val, idx in count.items():
            freqs[idx].append(val)
        
        for buc in range(len(freqs)-1, 0, -1):
            res.extend(freqs[buc])
            if len(res) == k:
                return res