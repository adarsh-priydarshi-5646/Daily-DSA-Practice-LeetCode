class Solution:
    def isPalindrome(self, s: str) -> bool:
        NewS = "".join(char for char in s if char.isalnum()).lower()
        n = len(NewS)
        def check_index(i: int) -> bool:
            if i >= n // 2:
                return True
            if NewS[i] != NewS[n - i - 1]:
                return False
            return check_index(i + 1) 
        return check_index(0)


        
        