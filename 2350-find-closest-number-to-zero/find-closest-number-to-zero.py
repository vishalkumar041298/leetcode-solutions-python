class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = float("inf")
        for i in nums:
            if abs(closest) > abs(i):
                closest = i
            elif abs(closest) == abs(i) and closest < i:
                closest = i
        return closest