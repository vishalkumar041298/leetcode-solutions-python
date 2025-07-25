class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        total = 0
        n = len(s)
    
        for i, v in enumerate(s):

            if i+1 < n and roman_map[s[i+1]] > roman_map[s[i]]:
                total-= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        return total