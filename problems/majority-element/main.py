from collections import defaultdict

class Solution:
    def majorityElement_brute(self, nums: list[int]) -> int:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        
        for k,v in freq.items():
            if v > len(nums) // 2:
                return k
        
        return -1
    
    def majorityElement_optimal(self, nums: list[int]) -> int:
        candidate = nums[0]
        count = 0

        for i in nums:
            if i == candidate:
                count += 1
            else:
                if count == 0:
                    candidate = i
                else:
                    count -= 1
        
        return candidate