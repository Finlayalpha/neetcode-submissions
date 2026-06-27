class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_count = {}

        sorted_nums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i] in seen_count:
                seen_count[nums[i]] += 1
            else: 
                seen_count[nums[i]] = 1
        
        sorted_dict = dict(sorted(seen_count.items(), key=lambda item: item[1], reverse=True))

        sorted_list = list(sorted_dict)

        result = []

        for j in range(0, k):
            result.append(sorted_list[j])
        
        return result