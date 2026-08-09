from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])                           # -- SORT First
        res = []
        res.append(intervals[0])

        for start, end in intervals[1:]:
            prev_end = res[-1][1]
            if start <= prev_end:
                res[-1][1] = max(prev_end,end)             # Why max : example: [1,9] [2,8] -> [1,9]
            else:
                res.append([start,end])
        return res 

sol = Solution()
assert (result:=sol.merge([[1,3],[2,6],[8,10],[15,18]])) == [[1,6],[8,10],[15,18]] , f'Failed, received:{result}'
assert (result:=sol.merge([[1,4],[4,5]])) == [[1,5]] , f'Failed, received:{result}'
assert (result:=sol.merge([[4,7],[1,4]])) ==  [[1,7]] , f'Failed, received:{result}'
