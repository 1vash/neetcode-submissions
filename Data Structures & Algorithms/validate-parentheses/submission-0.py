class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ']':'[', 
            '}':'{', 
            ')':'('
        }
        stack = []
        
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    # "[)"
                    return False  
                       
        return not stack
        