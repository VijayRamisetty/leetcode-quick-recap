class Solution(object):
    def longestCommonPrefix(self, strs):

        prefix = strs[0]
        for s in strs:
            if prefix == '':
                return ''
            while not s.startswith(prefix):
                prefix = prefix[:-1]
        return prefix

sol = Solution()
assert (result:=sol.longestCommonPrefix(["flower","flow","flight"])) == 'fl' , f'Failed, received:{result}'
assert (result:=sol.longestCommonPrefix(["dog","racecar","car"])) == "" , f'Failed, received:{result}'
