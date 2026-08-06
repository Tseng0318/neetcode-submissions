# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(low, high, node):
            if not node:
                return True
            if not (low<node.val<high):
                return False
            return (validate(low, node.val, node.left) and
            validate(node.val, high, node.right))
        return validate(float('-inf'), float('inf'), root)
        