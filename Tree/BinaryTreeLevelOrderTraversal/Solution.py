from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: TreeNode):
        # edge case if root is None
        if root is None:
            return []

        # even: left to right
        # odd: right to left
        level_order = {}
        queue = deque([(root, 0)])

        while len(queue) > 0:
            node, level = queue.popleft()
            # check if we need a new level
            if level not in level_order:
                level_order[level] = []

            # add node val to its corresponding level
            level_order[level].append(node.val)

            # check if children node on next level need to be added to queue for processing
            if node.left is not None:
                queue.append((node.left, level + 1))
            if node.right is not None:
                queue.append((node.right, level + 1))

        return level_order.values()
