from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        for i, n in enumerate(nums):
            
            if i==0 or n !=nums[i-1] +1:               #-- no previous sibling
                start = n
            
            if i==len(nums)-1 or n!=nums[i+1] -1:      #-- no next sibling
                if start == n:           #-- orphan
                    res.append(str(n))
                else:
                    res.append(f'{start}->{n}')
        return res 
    
sol = Solution()
assert (result:=sol.summaryRanges([0,1,2,4,5,7])) == ["0->2","4->5","7"] ,  f'Failed, received:{result}'
assert (result:=sol.summaryRanges([0,2,3,4,6,8,9])) == ["0","2->4","6","8->9"] ,  f'Failed, received:{result}'
