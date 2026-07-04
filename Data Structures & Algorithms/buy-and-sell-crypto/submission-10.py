class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        current = 0
        highest = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                current = prices[j] - prices[i]
                if current >= highest:
                    highest = current

        return highest
        