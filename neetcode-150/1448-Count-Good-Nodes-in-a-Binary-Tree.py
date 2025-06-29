# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0 
        def dfs(root, max_so_far):
            if root is None: return None
            if root.val >= max_so_far:
                self.ans += 1
                max_so_far = root.val
            dfs(root.left, max_so_far)
            dfs(root.right, max_so_far)
        dfs(root, float('-inf'))
        return self.ans

        # TC : O(n)
        # SC : O(h)