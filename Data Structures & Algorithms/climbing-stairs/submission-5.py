class Solution:
    def climbStairs(self, n: int) -> int:

        cache = {}

        def ways(n: int, i: int):

            if i in cache:
                return cache[i]

            if i == n:
                return 1

            if i > n:
                return 0

            ans = ways(n, i + 1) + ways(n, i + 2)

            cache[i] = ans

            return ans

        return ways(n, 0)