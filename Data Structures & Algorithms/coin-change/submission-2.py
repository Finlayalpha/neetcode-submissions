class Solution:
    def coinChange(self, coins: List[int], amount: int):

        cache = {}
        def remaining(total_value):

            if total_value in cache:
                return cache[total_value]

            if total_value == amount:
                return 0

            if total_value > amount:
                return float("inf")

            best = float("inf")

            for coin in coins:
                best = min(best, 1 + remaining(total_value + coin))
                cache[total_value] = best

            return best

        ans = remaining(0)
        return ans if ans != float("inf") else -1
