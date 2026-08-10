from typing import List
class Solution:
    def nextGreater(self, nums:List) -> List:
        stack = []
        res = [-1] * len(nums)
        for i, current_num in enumerate(nums):
            print(stack)
            while stack and current_num > nums[stack[-1][0]]:  # current_num > top_of_stack
                 popped_index, val = stack.pop()
                 res[popped_index] = current_num 
            stack.append((i,current_num))
        return res
sol = Solution()
assert (received:=sol.nextGreater([73,74,75,71,69,72,76,73])) == [74, 75, 76,72,72,76, -1 , -1], f'Failed {received=}'
print('-'*10)
assert (received:=sol.nextGreater([1, 3, 2, 4])) == [3, 4, 4, -1], f'Failed {received=}'
