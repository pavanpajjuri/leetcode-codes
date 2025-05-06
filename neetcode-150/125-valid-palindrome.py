class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for x in s:
            if x.isalnum():
                r += x.lower()
        return r == r[::-1]