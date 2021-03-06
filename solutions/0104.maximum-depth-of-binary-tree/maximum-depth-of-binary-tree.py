#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
from LeetCode_in_Python.datastruct.TreeNode import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# @lc code=end
