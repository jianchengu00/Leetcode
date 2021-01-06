# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: ListNode) -> ListNode:
        reversed_head = None
        curr = head
        while curr is not None:
            # save current node's next node
            next_node = curr.next
            # set current node to point to the head of the reversed list
            curr.next = reversed_head
            # update the new head on the reversed list
            reversed_head = curr
            # set current to the next node
            curr = next_node
        return reversed_head
