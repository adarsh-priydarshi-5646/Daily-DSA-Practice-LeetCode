class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            if n in seen:
                return False  # loop lag gaya
            seen.add(n)
            
            total = 0
            temp = n
            while temp > 0:
                digit = temp % 10       # last digit
                total += digit * digit  # square karke total me add
                temp = temp // 10       # digit hata do
            
            n = total  # n ko update karo

        return True  # agar n == 1 ho gaya
        