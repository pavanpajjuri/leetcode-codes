from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        q = deque([])

        tc = m*n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    tc -= 1
                    
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        time = 0
        while q:
            tc -= len(q)
            for _ in range(len(q)):
                u,v = q.popleft()
                for du,dv in [[-1,0],[1,0],[0,1],[0,-1]]:
                    r,c = u+du, v+dv
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
            time += 1
        
        return max(0,time-1) if tc == 0 else -1

        # TC : O(m*n)
        # SC : O(m*n)