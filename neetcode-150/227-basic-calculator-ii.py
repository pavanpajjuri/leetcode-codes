class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        curr = ""
        sign = '+'
        st = []
        
        for i,ch in enumerate(s):
            if ch in '0123456789':
                curr += ch
                # num = num*10 + int(ch)
                
            if ch in '+-*/' or i == len(s)-1:
                curr = int(curr)
                if sign == '+':
                    st.append(curr)
                elif sign == '-':
                    st.append(-curr)
                elif sign == '*':
                    st.append(st.pop()*curr)
                else:
                    st.append(int(st.pop()/curr))
                sign = ch
                curr = ""

        return sum(st)