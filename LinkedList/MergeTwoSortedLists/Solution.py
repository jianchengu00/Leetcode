# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0, None)
        tail = head

        while True:
            # if one list runs out, then just append the rest of the other list
            if l1 is not None:
                tail.next = l2
                break
            if l2 is not None:
                tail.next = l1
                break

            # compare the current nodes of each list
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            else:
                tail.next = l2
                l2 = l2.next
                tail = tail.next

        return head.next
