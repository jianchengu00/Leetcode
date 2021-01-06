# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        # dictionary to store the memory addresses of each node
        node_dict = {}
        curr = head
        while curr is not None:
            # check if the current node has already been seen/stored in the dictionary
            if id(curr) in node_dict:
                return True
            node_dict[id(curr)] = 1
            curr = curr.next
        return False
