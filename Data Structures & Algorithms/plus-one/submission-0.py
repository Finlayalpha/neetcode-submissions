class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = int("".join(str(digit) for digit in digits))
        num += 1

        output = []
        for char in str(num):
            output.append(char)
        
        return output
        