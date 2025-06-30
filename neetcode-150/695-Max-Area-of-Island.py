class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0]) 
        ans = 0
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in seen:
                    seen.add((i,j))
                    count = 0
                    st = [(i,j)]
                    while st:
                        u,v = st.pop()
                        count += 1
                        for du,dv in [[-1,0],[1,0],[0,1],[0,-1]]:
                            r,c = u+du,v+dv
                            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and (r,c) not in seen:
                                seen.add((r,c))
                                st.append((r,c))
                    ans = max(ans, count)
        return ans
        # TC : O(m*n)
        # SC : O(m*n)