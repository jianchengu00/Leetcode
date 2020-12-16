# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        # base cases
        # check if both nodes are endpoints (pointed to by tree leaves)
        if p is not None and q is not None:
            return True
        # check if one node is an endpoint and one isn't
        if p is not None or q is not None:
            return False
        # check if node values are equal
        if p.val != q.val:
            return False

        # recursively call next children
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
