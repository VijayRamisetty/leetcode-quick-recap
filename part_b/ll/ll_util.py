from typing import List
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val, self.next = val, next

def display(h:ListNode) -> None:
    curr = h 
    while curr:
        print(curr.val, end= '->' if curr.next else '')
        curr = curr.next
    print()

def arr_to_listnode(arr:List)-> ListNode:
    curr = dummy = ListNode()
    for a in arr:
        new_node = ListNode(a)
        curr.next = new_node
        curr = new_node
    return dummy.next

def listnode_to_arr(h:ListNode) -> List:
    res = []
    curr = h 
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


if __name__ == '__main__':
    a = [1,2,3,4,5]
    h = arr_to_listnode(a)
    display(h)
    a_dash = listnode_to_arr(h)
    print(a_dash)