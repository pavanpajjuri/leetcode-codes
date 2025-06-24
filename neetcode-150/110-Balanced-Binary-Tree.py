class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def dfs(root):
            if root is None:
                return 0
            l_h = dfs(root.left)
            r_h = dfs(root.right)
            if abs(r_h-l_h) > 1:
                self.balanced = False
            return 1 + max(l_h,r_h)
        dfs(root)
        return self.balanced

        # TC : O(n)
        # SC : O(n)