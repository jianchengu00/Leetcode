import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_k_lists(self, lists: list) -> ListNode:
        head = ListNode(0)
        curr = head

        # set up priority queue for picking the smallest of each first list element
        # use each list's index to access their current heads
        pq = [(l_head.val, idx) for idx, l_head in enumerate(lists) if l_head is not None]
        heapq.heapify(pq)

        while len(pq) > 0:
            # get smallest valued head of all the lists using min heap
            val, idx = heapq.heappop(pq)
            # add node to merged list
            curr.next = ListNode(val)
            # update the current pointer for the merged list
            curr = curr.next
            # get the next node in the list for the popped list from above
            lists[idx] = lists[idx].next
            if lists[idx] is not None:
                heapq.heappush(pq, (lists[idx].val, idx))

        return head.next
