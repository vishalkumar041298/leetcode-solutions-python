class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float("inf")
        for n in nums:
            if abs(closest) == abs(n) and closest < n:
                closest = n
            elif abs(closest) > abs(n):
                closest = n
                
        return closest