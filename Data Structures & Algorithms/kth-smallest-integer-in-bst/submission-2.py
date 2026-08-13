# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        
        def inorder(node):
            if not node:
                return 
            inorder(node.left)              # go left first
            self.k -= 1
            if self.k == 0:
                self.result = node.val     # this is the answer
                return
            inorder(node.right)              # then right
        
        inorder(root)
        return self.result