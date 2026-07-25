class Solution:
    def rob(self, nums: List[int]) -> int:

        seen = {}
        def rec(house):

            if house >= len(nums):
                return 0
                
            if house in seen:
                return seen[house]

            seen[house] = max(
                nums[house] + rec(house + 2), 
                rec(house + 1)
            )

            return seen[house]

        return rec(0)





        