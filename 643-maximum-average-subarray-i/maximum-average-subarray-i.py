class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        
        total = sum(nums[:k])
        maxavg = total
        for r in range(k, n):
            total = total - nums[r-k] + nums[r]
            maxavg = max(total, maxavg)

        return maxavg/k
        