from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height)-1
        while l<r:
            length = min(height[l], height[r]) 
            breadth = r-l
            area = length * breadth
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_area

sol = Solution()
assert (received:=sol.maxArea(height = [1,8,6,2,5,4,8,3,7] )) == 49, f'Failed {received= }'
assert (received:=sol.maxArea(height = [1,1])) == 1, f'Failed {received= }'