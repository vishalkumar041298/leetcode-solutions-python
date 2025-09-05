# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        def has_sum(cur_sum, node):
            if not node:
                return False
            
            cur_sum += node.val
            if not node.left and not node.right:
                return cur_sum == targetSum

            return has_sum(cur_sum, node.left) or has_sum(cur_sum, node.right)
        return has_sum(0, root)
