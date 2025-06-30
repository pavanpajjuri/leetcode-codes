class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m,n = len(grid), len(grid[0])
        count = 0
        st = []
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in seen:
                    count += 1
                    seen.add((i,j))
                    st.append((i,j))
                    while st:
                        u,v = st.pop()
                        for du,dv in [[-1,0],[1,0],[0,-1],[0,1]]:
                            r = u + du
                            c = v + dv
                            if 0<=r<m and 0<=c<n and grid[r][c] == "1" and (r,c) not in seen:
                                seen.add((r,c))
                                st.append((r,c))
        return count
    # TC : O(m*n)
    # SC : O(m*n)
        