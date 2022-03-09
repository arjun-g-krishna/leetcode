class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in dictionary:
                if stack and stack[-1] == dictionary[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        if not stack:
            return True
        else:
            return False