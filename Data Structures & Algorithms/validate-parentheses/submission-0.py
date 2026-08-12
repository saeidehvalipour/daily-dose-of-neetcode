class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            # if opening bracket → push
            if ch in pairs.values():
                stack.append(ch)
            else:
                # if closing bracket → stack must not be empty
                if not stack:
                    return False
                
                # check matching pair
                if stack[-1] != pairs[ch]:
                    return False
                
                stack.pop()
        
        # stack must be empty at end
        return len(stack) == 0
    
        