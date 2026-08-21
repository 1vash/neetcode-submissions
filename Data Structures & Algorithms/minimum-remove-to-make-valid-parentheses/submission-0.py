# "nee(t(c)o)de)"
# "nee(t(c)o)de"

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        # 1st pass: remove excess ')'
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
                stack.append(char)  # always include '('
            elif char == ')':
                if balance > 0:
                    # if balance > 0 and ")" appears then it means everything is correct, 
                    # we should add this parentesis
                    balance -= 1
                    stack.append(char)
                # else: skip the ')' because it's unmatched
            else:
                # we should skip only non-balanced parenthesis but always include chars
                stack.append(char)
        
                # 2nd pass: remove excess '(' from the end
        if balance > 0:
            for i in range(len(stack)-1,-1,-1):
                if stack[i] == '(' and balance > 0:
                    balance -= 1
                    del stack[i]
        
        return "".join(stack)