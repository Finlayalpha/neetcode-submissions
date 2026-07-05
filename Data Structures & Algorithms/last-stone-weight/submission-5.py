class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1:
            return stones[0]
        elif not stones:
            return 0
        else:
            while len(stones) > 1:
                stones = sorted(stones)
                big, small = stones[-1], stones[-2]
                if big == small:
                    stones.remove(big)
                    stones.remove(small)
                elif big > small:
                    remainder = big - small
                    stones[-1] = remainder
                    stones.remove(small)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0
            
            
