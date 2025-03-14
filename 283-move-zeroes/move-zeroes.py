class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l = 0
        # r = len(nums) - 1
        # while l< r:
        #     if nums[l] == 0 and nums[r]!= 0:
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l+=1
        #         r-=1
        #     if nums[r]== 0:
        #         r-=1
        #     if nums[l]!=0:
        #         l+=1
        l = 0
        for r in range(len(nums)):
            
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
