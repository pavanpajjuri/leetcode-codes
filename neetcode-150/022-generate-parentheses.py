class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def validParenthesis(curr, op, cl):
            if op == cl == n:
                ans.append(curr)
                return
            if op < n:
                validParenthesis(curr+"(", op+1, cl)
            if cl < op:
                validParenthesis(curr+")", op, cl+1)
        validParenthesis("", 0, 0)    
        return ans