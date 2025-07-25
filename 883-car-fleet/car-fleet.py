class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(zip(position, speed), reverse=True)

        stack = []

        for p, s in ps:
            tt = (target-p)/s
            if not stack or tt>stack[-1]:
                stack.append(tt)
        return len(stack)