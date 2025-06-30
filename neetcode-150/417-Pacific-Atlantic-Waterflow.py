from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        p = deque()
        p_seen = set()
        a = deque()
        a_seen = set()


        for i in range(m):
            p.append((i,0))
            p_seen.add((i,0))
            a.append((i,n-1))
            a_seen.add((i,n-1))
        
        for i in range(n):
            p.append((0,i))
            p_seen.add((0,i))
            a.append((m-1,i))
            a_seen.add((m-1,i))
        
        while p:
            u,v = p.popleft()
            for du,dv in [[-1,0],[1,0],[0,-1],[0,1]]:
                r, c = u+du, v+dv
                if 0 <= r < m and 0 <= c < n and (r,c) not in p_seen and heights[r][c] >= heights[u][v]:
                    p_seen.add((r,c))
                    p.append((r,c))
        
        while a:
            u,v = a.popleft()
            for du,dv in [[-1,0],[1,0],[0,-1],[0,1]]:
                r, c = u+du, v+dv
                if 0 <= r < m and 0 <= c < n and (r,c) not in a_seen and heights[r][c] >= heights[u][v]:
                    a_seen.add((r,c))
                    a.append((r,c))
        
        return list(p_seen.intersection(a_seen))


        #TC : O(m*n)
        #SC : O(m*n)