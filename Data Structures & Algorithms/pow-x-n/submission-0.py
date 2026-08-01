class Solution:
    def myPow(self, x: float, n: int) -> float:

        value = 1

        for i in range(1, abs(n) + 1):

            if n < 0:
                value *= 1 / x
            else:
                value *= x

        return value
        