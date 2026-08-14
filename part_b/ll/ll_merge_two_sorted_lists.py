from typing import Optional
from ll_util import ListNode, arr_to_listnode, listnode_to_arr
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        curr = dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = ListNode(l1.val)
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                curr = curr.next
                l2 = l2.next
        curr.next = l1 or l2
        return dummy.next


sol = Solution()
assert (received:=listnode_to_arr(sol.mergeTwoLists(
list1 = arr_to_listnode([1,2,4]),
list2 = arr_to_listnode([1,3,4])
))) == [1,1,2,3,4,4], f'Failed : {received=}'

assert (received:=listnode_to_arr(sol.mergeTwoLists(
list1 = arr_to_listnode([]),
list2 = arr_to_listnode([])
))) == [], f'Failed : {received=}'

assert (received:=listnode_to_arr(sol.mergeTwoLists(
list1 = arr_to_listnode([]),
list2 = arr_to_listnode([0])
))) == [0], f'Failed : {received=}'
