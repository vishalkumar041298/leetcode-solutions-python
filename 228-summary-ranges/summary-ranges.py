class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res = []

        for n in nums:
            if res and res[-1][1] +1 == n:
                res[-1][1] = n
            else:
                res.append([n, n])
        
        return [f'{x}->{y}' if x!=y else f'{x}' for x, y in res]