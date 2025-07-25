class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            print(i, stack)
            if i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(stack[-1]*2)
            elif i == '+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
            else:
                stack.append(int(i))
        return sum(stack)