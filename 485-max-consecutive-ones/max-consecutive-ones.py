class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        count = 0
        for num in nums:
            if num:
                count+=1
                max_cons = max(count, max_cons)
            else:
                count = 0
        return max_cons