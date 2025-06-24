class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def dfs(root):
            if root is None:
                return 0
            l_h = dfs(root.left)
            r_h = dfs(root.right)
            self.max_diameter = max(self.max_diameter, l_h + r_h) 
            return 1 + max(l_h,r_h)
        dfs(root)
        return self.max_diameter

        # TC : O(n)
        # SC : O(n)
        