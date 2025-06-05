class Solution:
    def isValid(self, s: str) -> bool:

        closed = {'}': '{', ')': '(', ']': '['}

        stack = []

        for i in s:
            if i not in closed:
                stack.append(i)
            elif not stack:
                return False
            else:
                last = stack.pop()
                if  closed[i] !=  last:
                    return False
        if not stack:
            return True
        return False

        