class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)

        window = defaultdict(int)
        res = [-1, -1]
        min_w = float('inf')

        l = 0
        have = 0
        need = len(countT)
        for r in range(len(s)):

            c = s[r]
            window[c] += 1
            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                if min_w > (r-l+1):
                    min_w = r-l+1
                    res  = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r+1] if min_w != float('inf') else ''
