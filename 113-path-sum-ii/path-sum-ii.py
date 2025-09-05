# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res, path = [], []

        def dfs(node, rem):
            if node is None:
                return
            path.append(node.val)
            rem -= node.val

            if node.left is None and node.right is None:
                if rem == 0:
                    res.append(path.copy())
            else:
                dfs(node.left, rem)
                dfs(node.right, rem)
            
            path.pop()
        dfs(root, targetSum)
        return res