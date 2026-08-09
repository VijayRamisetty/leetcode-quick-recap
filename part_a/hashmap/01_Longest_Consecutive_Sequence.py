from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            if n-1 not in numSet:      # if no previous sibling, that's the start
                count = 0
                while n+count in numSet:   # REMEMBER : n + count
                    count +=1
                longest = max(longest, count)
        return longest



sol = Solution() 
# -- unsorted array of integers, can contains duplicates too
assert (received:=sol.longestConsecutive([100,4,200,1,3,2])) == 4, f'Failed: {received=}'
assert (received:=sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) == 9, f'Failed: {received=}'
assert (received:=sol.longestConsecutive([1,0,1,2])) == 3, f'Failed: {received=}'
