class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            big, small = stones[-1], stones[-2]
            if big == small:
                stones.pop()
                stones.pop()
            elif big > small:
                remainder = big - small
                stones[-1] = remainder
                stones.remove(small)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0
            
            
