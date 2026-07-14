# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            left_d = depth(node.left) # 3
            right_d = depth(node.right) 
            # Update the outer diameter tracker
            self.diameter = max(self.diameter, left_d+right_d)
            # Return the depth
            return 1 + max(left_d, right_d)
        
        depth(root)
        return self.diameter
        