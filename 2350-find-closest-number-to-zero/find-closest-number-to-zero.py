class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float('inf')

        for num in nums:
            if abs(num) <= abs(closest):
                if abs(num) == abs(closest):
                    closest = max(closest, num)
                else:
                    closest = num
        return closest