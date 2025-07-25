class Solution:
    def isValid(self, s: str) -> bool:
        closed = {'}': '{', ')': '(', ']': '['}
        stack = []

        for c in s:
            if c not in closed:
                stack.append(c)
            elif not stack:
                return False
            else:
                last = stack.pop()
                if last != closed[c]:
                    return False
        if not stack:
            return True
        return  False