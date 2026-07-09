import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        self.topk = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.topk) < self.k:
            heapq.heappush(self.topk, val)

        elif val > self.topk[0]:
            heapq.heapreplace(self.topk, val)

        return self.topk[0]