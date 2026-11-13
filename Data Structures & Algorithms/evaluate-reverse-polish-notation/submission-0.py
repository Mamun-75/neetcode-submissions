class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                temres = stack.pop() + stack.pop()
                stack.append(temres)
             
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                temres = b - a
                stack.append(temres)
            
            elif c =="*":
                a = stack.pop()
                b = stack.pop()
                temres = b * a
                stack.append(temres)
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                temres = int((float (b)/a))
                stack.append(temres)
            else:
                stack.append(int(c))
        return stack[0]           


        