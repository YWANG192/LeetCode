# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
        
        return self.recur(root.left, root.right)
        
        
        
    def recur (self, left, right):
        if left is None and right is None:
            return True

        if left is None or right is None or left.val != right.val:
            return False

        return self.recur(left.left, right.right) and self.recur(left.right, right.left)
