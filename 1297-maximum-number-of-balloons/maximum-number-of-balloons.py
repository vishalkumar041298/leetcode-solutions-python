class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mc = Counter('balloon')
        tc = Counter(text)

        min_count = float('inf')

        for t, val in mc.items():
            if t not in tc:
                return 0
            min_count = min(tc[t]//val, min_count)
        return min_count