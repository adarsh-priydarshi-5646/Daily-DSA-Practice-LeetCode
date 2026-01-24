class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {

            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
            
        num = 0
        prev_value = 0
        for char in s[::-1]:
            current_value = romans[char]
                # If the current value is smaller than the previous value, subtract it
            if current_value < prev_value:
                num -= current_value
            else:
                num += current_value
                
                # Update the previous value
            prev_value = current_value
        return num