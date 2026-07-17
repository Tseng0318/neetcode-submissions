# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return 0
            
            left = depth(node.left)
            if left==-1:            # left unbalanced → propagate
                return -1
            
            right = depth(node.right)
            if right==-1:            # right unbalanced → propagate
                return -1
            
            if abs(right - left) > 1:            # this node's imbalance
                return -1
            
            return 1+max(left, right)
        
        return depth(root) != -1
            
        
        