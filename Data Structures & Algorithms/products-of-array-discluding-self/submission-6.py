class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []

        for i in range(len(nums)):
            exc = nums[:i] + nums[i + 1:]
            prod = 1
            for j in exc:
                prod *= j
            result.append(prod)

        return result