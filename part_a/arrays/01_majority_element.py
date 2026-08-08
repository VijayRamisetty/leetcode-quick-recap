class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for n in nums:
            if count == 0: candidate = n
            count +=( 1 if candidate == n else -1)
        return candidate


sol = Solution()
assert (result:=sol.majorityElement([3,2,3])) == 3, f'Failed, received is {result}'
assert (result:=sol.majorityElement([2,2,1,1,1,2,2])) == 2, f'Failed, received is {result}'
