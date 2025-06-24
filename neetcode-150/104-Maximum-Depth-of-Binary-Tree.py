class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, height):
            if root is None:
                return height
            return max(dfs(root.left, height + 1), dfs(root.right, height + 1))
        height = dfs (root, 0)
        return height

        # TC : O(n)
        # SC : O(n)