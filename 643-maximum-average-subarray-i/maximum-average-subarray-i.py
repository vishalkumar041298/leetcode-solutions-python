class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        n = len(nums)
        
        total = sum(nums[:k])
        maxavg = total
        for r in range(k, n):
            total = total - nums[l] + nums[r]
            l += 1
            aavg = total
            maxavg = max(aavg, maxavg)

        return maxavg/k
        