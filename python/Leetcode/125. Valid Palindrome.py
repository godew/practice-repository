class Solution:
    def isPalindrome(self, s: str) -> bool:

        tmp = ""

        for c in s:
            if c.isalnum():
                tmp += c

        tmp = tmp.lower()
        
        return tmp[::-1] == tmp