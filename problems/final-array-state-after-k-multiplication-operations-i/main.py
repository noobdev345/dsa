import heapq

class Solution:
    def getFinalState_brute(self, nums: list[int], k: int, x: int) -> list[int]:
        for i in range(k):
            mini = min(nums)
            for j in range(len(nums)):
                if nums[j] == mini:
                    nums[j] *= x
                    break
        return nums
    
    def getFinalState_optimal(self, nums: list[int], k: int, x: int) -> list[int]:
        min_heap = [(num, idx) for (idx, num) in enumerate(nums)]
        heapq.heapify(min_heap)

        for _ in range(k):
            num, i = heapq.heappop(min_heap)
            nums[i] *= x
            heapq.heappush(min_heap, (nums[i], i))
            
        return nums
    