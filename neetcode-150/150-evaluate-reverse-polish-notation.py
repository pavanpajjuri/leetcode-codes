class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for x in tokens:
            if x not in '+-*/':
                st.append(int(x))
            else:
                val2 = st.pop()
                val1 = st.pop()
                if x == '+':
                    st.append(val1+val2)
                elif x == '-':
                    st.append(val1-val2)
                elif x == '*':
                    st.append(val1*val2)
                else:
                    st.append(int(val1/val2))
        
        return st[-1]
        