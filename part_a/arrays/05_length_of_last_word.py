class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l, r = 0, len(s) -1
        while l<=r and s[r] ==' ':        # While True space -- move backwards
            r -=1
        counter =0 
        while l<=r and s[r] !=' ':        # move backwards Till no space
            r-=1
            counter +=1
        return counter

sol = Solution()
assert (result:=sol.lengthOfLastWord("Hello World")) == 5,  f'Failed, received:{result}'
assert (result:=sol.lengthOfLastWord("   fly me   to   the moon  ")) == 4,  f'Failed, received:{result}'
assert (result:=sol.lengthOfLastWord("luffy is still joyboy")) == 6,  f'Failed, received:{result}'

        