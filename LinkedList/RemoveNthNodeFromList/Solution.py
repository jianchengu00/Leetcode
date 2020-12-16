# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_from_end(self, head: ListNode, n: int) -> ListNode:
        # find the length of the list
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next

        # find the target node to stop at, which is the node
        # before the one we want to delete
        target = length - n

        # update pointers until we have pointers to the target node
        # as well as the node to delete
        curr = head
        prev = None
        while target > 0:
            prev = curr
            curr = curr.next
            target -= 1

        # delete the node
        # if the node to delete is the first node, then just set it to its next node
        if prev is not None:
            head = head.next
        else:
            prev.next = curr.next
        return head
