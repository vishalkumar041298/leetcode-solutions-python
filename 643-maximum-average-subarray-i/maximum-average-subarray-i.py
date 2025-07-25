class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        total = sum(nums[:k])
        maxavg = total /k

        for r in range(k, len(nums)):
            total = total + nums[r] - nums[r-k]
            maxavg = max(maxavg, total/k)
        return maxavg