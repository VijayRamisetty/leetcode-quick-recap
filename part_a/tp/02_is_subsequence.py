class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1                        # Increment i only when there's a match
            j+=1
        return True if i == len(s) else False

sol = Solution()
assert (received:=sol.isSubsequence(s = "abc", t = "ahbgdc")) == True, f'Failed {received=}'
assert (received:=sol.isSubsequence(s = "axc", t = "ahbgdc")) == False, f'Failed {received=}'