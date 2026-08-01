class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while n != 1:

            new = 0

            digits = [int(digit) for digit in str(n)]

            for digit in digits:
                new += digit ** 2
            
            if new in seen:
                return False

            seen.add(new)

            n = new

        return True

        
