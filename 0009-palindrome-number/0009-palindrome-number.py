class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverseNumber = 0
        if x < 0:
            return False
        newX = x
        while newX > 0:
            digit = newX % 10
            reverseNumber = (reverseNumber * 10) + digit
            newX //= 10
        if x == reverseNumber:
            return True
        else:
            return False