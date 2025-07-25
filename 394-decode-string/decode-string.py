class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curnum = 0
        curstr = ''

        for c in s:
            if c == ']':
                num = stack.pop()
                prevstr = stack.pop()
                curstr = prevstr + curstr*num
            elif c=='[':
                stack.append(curstr)
                stack.append(curnum)
                curnum = 0
                curstr = ''
            elif c.isdigit():
                curnum = curnum*10 + int(c)
            else:
                curstr += c
        return curstr