class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n%2 == 1:
            return False

        braces = {
            '}':'{',
            ')':'(',
            ']':'['
            }
        
        st = []
        for x in s:
            if x not in braces:
                st.append(x)
            else:
                if not st or st[-1] != braces[x]:
                    return False
                else:
                    st.pop()
        return len(st) == 0