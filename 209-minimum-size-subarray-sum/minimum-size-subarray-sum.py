class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        r = 0
        total = 0
        min_len = float('inf')
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                min_len = min(min_len, r-l + 1)
                total -= nums[l]
                l += 1
        return min_len if min_len != float('inf') else 0