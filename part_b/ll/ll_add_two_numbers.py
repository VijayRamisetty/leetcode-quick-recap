from typing import List
from ll_util import ListNode, display, arr_to_listnode, listnode_to_arr
class Solution(object):
    def addTwoNumbers(self, l1:ListNode, l2:ListNode):
        curr = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            that_sum = a + b + carry
            carry, val = divmod(that_sum, 10)
            new_node = ListNode(val)
            curr.next = new_node
            curr = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next




sol = Solution()
assert (received:=listnode_to_arr(
    sol.addTwoNumbers(
    l1 = arr_to_listnode([2,4,3]),
    l2 = arr_to_listnode([5,6,4]))
)) == [7,0,8], F'Failed {received=}'
assert (received:=listnode_to_arr(
    sol.addTwoNumbers(
    l1 = arr_to_listnode([0]),
    l2 = arr_to_listnode([0])))
) ==  [0], F'Failed {received=}'
assert (received:=listnode_to_arr(
    sol.addTwoNumbers(
    l1 = arr_to_listnode([9,9,9,9,9,9,9]), 
    l2 = arr_to_listnode([9,9,9,9])))
)== [8,9,9,9,0,0,0,1], F'Failed {received=}'