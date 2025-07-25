class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_length = float('-inf')
        longest = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            max_length = max(freq[s[r]], max_length)
            curr = r - l + 1
            if curr - max_length > k:
                freq[s[l]] -= 1
                l += 1
            
            longest = max(longest, r-l+1)
        return longest
