class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        digits = {
            "0": 0, 
            "1": 1, 
            "2": 2, 
            "3": 3, 
            "4": 4, 
            "5": 5, 
            "6": 6, 
            "7": 7, 
            "8": 8, 
            "9": 9,
            }
        
        value1 = []
        value2 = []

        for digit in num1:
            value1.append(digits[digit])
        for digit in num2:
            value2.append(digits[digit])

        value1 = int("".join(map(str, value1)))
        value2 = int("".join(map(str, value2)))

        prod = value1 * value2

        return str(prod)

        