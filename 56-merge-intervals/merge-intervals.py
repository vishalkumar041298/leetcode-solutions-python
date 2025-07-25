class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])

        for start, end in intervals:
            if res and res[-1][0] <= start and res[-1][1] >= start:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])
        return res