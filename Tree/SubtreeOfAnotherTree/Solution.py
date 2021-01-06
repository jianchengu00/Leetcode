# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False
        if self.same_tree(s, t):
            return True
        return self.is_subtree(s.left, t) or self.is_subtree(s.right, t)

    def same_tree(self, s: TreeNode, t: TreeNode) -> bool:
        # if both are leaves, then they are the same
        if s is None and t is None:
            return True
        # if only one is a leaf, or their values don't match, then they are not the same
        if s is None or t is None:
            return False
        if s.val != t.val:
            return False

        return self.same_tree(s.left, t.left) and self.same_tree(s.right, t.right)
