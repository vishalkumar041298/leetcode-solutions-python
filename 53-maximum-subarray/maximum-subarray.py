class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = float('-inf')

        total = 0

        for num in nums:
            total += num
            largest = max(total, largest)
            if total < 0:
                total = 0
            
            
        return largest