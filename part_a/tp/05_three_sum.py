class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()                                     #-- SORT first
        res = []
        for i, a in enumerate(nums):

            if i>0 and nums[i] == nums[i-1]:            #-- present  == previous SKIP
                continue

            l, r = i+1 , len(nums)-1                    #--  WHY l = i+1 , Cause current is 'a' 
            while l<r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -=1
                elif three_sum <0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    
                    while l<r and nums[l] == nums[l-1]:     #-- present == previous ( move + )
                        l+=1
        return res

sol = Solution()
assert((received:=sol.threeSum(nums = [-1,0,1,2,-1,-4]))) == [[-1,-1,2],[-1,0,1]], f'Failed {received=}'
assert((received:=sol.threeSum(nums = [0,1,1]))) == [], f'Failed {received=}'
assert((received:=sol.threeSum(nums = [0,0,0]))) == [[0,0,0]], f'Failed {received=}'
