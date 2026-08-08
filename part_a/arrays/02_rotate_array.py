class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def do_rotate(l, r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        k = k % len(nums)
        l, r = 0, len(nums) -1
        do_rotate(l,r)
        do_rotate(l, k-1)
        do_rotate(k, r)
        return nums

s = Solution()
result = s.rotate([1,2,3,4,5,6,7], 3)
assert  result == [5,6,7,1,2,3,4] , f'Failed, received is {result}'
result = s.rotate([-1,-100,3,99], 2)
assert result == [3,99,-1,-100] , f'Failed, received is {result}'
