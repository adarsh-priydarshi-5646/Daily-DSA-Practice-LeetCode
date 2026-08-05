class Solution:
    def reverse(self, x: int) -> int:
        orignalX = x
        if x < 0:
            x = -(x)
        reverseNumber = 0
        while x > 0:
            lastdigit = x % 10
            reverseNumber  = (reverseNumber * 10) + lastdigit
            x //= 10
        if reverseNumber < -2147483648 or reverseNumber > 2147483647:
            return 0
        if orignalX < 0:
            return -(reverseNumber)
        return reverseNumber
        