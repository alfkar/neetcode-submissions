# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    fullTreeBalanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDepth(root)
        return self.fullTreeBalanced 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        if abs(leftDepth - rightDepth) >= 2:
            self.fullTreeBalanced = False
        return 1 + max(leftDepth, rightDepth)


