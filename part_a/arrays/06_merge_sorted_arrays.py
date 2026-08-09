class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        i = m + n - 1
        while p2>=0:                                    # while p2>=0 
            if p1>=0 and nums1[p1] > nums2[p2]:             # if p1>=0
                nums1[i] = nums1[p1]
                p1 -=1
            else:
                nums1[i] = nums2[p2]
                p2 -=1
            i -=1

        return nums1

sol = Solution()
assert (result:=sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)) == [1,2,2,3,5,6], f'Failed, received:{result}'
assert (result:=sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0)) == [1], f'Failed, received:{result}'
assert (result:=sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)) == [1], f'Failed, received:{result}'




