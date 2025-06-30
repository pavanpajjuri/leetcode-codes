class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n = len(board), len(board[0])
        # seen = set()
        st = []
        for i in range(m):
            if board[i][0]=="O":
                # seen.add((i,0))
                board[i][0] = "T"
                st.append((i,0))
            if board[i][n-1] == "O":
                # seen.add((i,n-1))
                board[i][n-1] = "T"
                st.append((i,n-1))
        for j in range(1,n-1):
            if board[0][j] == "O":
                # seen.add((0,j))
                board[0][j] = "T"
                st.append((0,j))
            if board[m-1][j] == "O":
                # seen.add((m-1,j))
                board[m-1][j] = "T"
                st.append((m-1,j))
        
        while st:
            u,v = st.pop()
            for du,dv in [[-1,0],[1,0],[0,1],[0,-1]]:
                r, c = u+du, v+dv
                if 0 <= r < m and 0 <= c < n and board[r][c] == "O": #and (r,c) not in seen:
                    # seen.add((r,c))
                    board[r][c] = "T"
                    st.append((r,c))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" :#and (i,j) not in seen:
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"

        # TC : O(m*n)
        # SC : O(m*n)
        