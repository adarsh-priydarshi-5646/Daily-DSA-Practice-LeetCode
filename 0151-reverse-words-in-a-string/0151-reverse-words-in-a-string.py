class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        b = a[::-1]
        return " ".join(b)  
        