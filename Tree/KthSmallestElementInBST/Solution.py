# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        vals = []
        self.traverse(root, vals)
        return vals[k - 1]

    def traverse(self, root, vals):
        if root is not None:
            self.traverse(root.left, vals)
            vals.append(root.val)
            self.traverse(root.right, vals)
