class Solution(object):
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        for i in range(m - n + 1):               # no point in checking beyond  (m-n+1)
            if haystack[i:i+n] == needle:
                return i
        return -1
    
sol = Solution()
assert (result:=sol.strStr(haystack="sadbutsad", needle="sad")) == 0 , f'Failed, received:{result}'
assert (result:=sol.strStr(haystack="leetcode", needle="leeto")) == -1 , f'Failed, received:{result}'
