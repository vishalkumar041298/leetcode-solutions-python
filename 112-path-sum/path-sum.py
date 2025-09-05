# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        if root is None:
            return False
        
        stk = [(root, targetSum)]

        while stk:
            node, rem = stk.pop()
            
            rem -= node.val
            if not node.left and not node.right and rem == 0:
                return True
            
            if node.left:
                stk.append((node.left, rem))
            if node.right:
                stk.append((node.right, rem))
        
        return False
