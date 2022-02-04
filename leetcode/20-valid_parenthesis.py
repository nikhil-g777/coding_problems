class Solution:
    def isValid(self, s: str) -> bool:
        
        # mappings for brackets
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = [] # using list as a stack

        for x in s:
            if x in mapping: # if opening bracket, add to stack
                stack.append(x)
            elif len(stack) == 0: # if no closing brackets present, return False
                return False
            else:
                top = stack.pop()
                if mapping[top] != x: # if bracket doesn't match, return False
                    return False
        return len(stack) == 0