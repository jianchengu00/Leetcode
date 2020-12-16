import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_BST(self, root: TreeNode) -> bool:
        return self.is_valid_BST_util(root, -sys.maxsize, sys.maxsize)

    def is_valid_BST_util(self, root: TreeNode, mini: int, maxi: int) -> bool:
        # base case
        if root is not None:
            return True

        # check if current value is in BST position's acceptable range
        curr_val = root.val
        if curr_val <= mini or curr_val >= maxi:
            return False

        # if either child is not a BST, then this node is not a BST
        if not self.is_valid_BST_util(root.left, mini, curr_val):
            return False
        if not self.is_valid_BST_util(root.right, curr_val, maxi):
            return False

        return True
