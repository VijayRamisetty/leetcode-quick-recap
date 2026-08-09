class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        for b in s:
            if b in lookup.values():
                stack.append(b)
            elif stack and stack[-1] == lookup[b]:
                stack.pop()
            else:
                return False
        return stack == []

sol = Solution()
assert (received:=sol.isValid("()")) == True, f'Failed: {received=}'
assert (received:=sol.isValid("()[]{}")) == True, f'Failed: {received=}'
assert (received:=sol.isValid("(]")) == False, f'Failed: {received=}'
assert (received:=sol.isValid("([])")) == True, f'Failed: {received=}'
assert (received:=sol.isValid("([)]")) == False, f'Failed: {received=}'
