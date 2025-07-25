class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = set(nums)
        longest = 0
        for n in num_map:
            if n-1 in num_map:
                continue
            count = 1
            while n + count in num_map:
                count+=1 
            longest = max(count, longest)
        
        return longest