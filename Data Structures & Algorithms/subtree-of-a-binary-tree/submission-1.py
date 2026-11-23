# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False
        if root.val == subRoot.val:
            result = self.compareSubRoot(root, subRoot)
            if result:
                return result
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)
        return left or right
    def compareSubRoot(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        leftResult = self.compareSubRoot(p.left,q.left)
        rightResult = self.compareSubRoot(p.right,q.right)
        currentNodes = q.val == p.val
        return leftResult and rightResult and currentNodes