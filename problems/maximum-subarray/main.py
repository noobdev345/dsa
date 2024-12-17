class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = -10001
        curr_sum = 0

        for i in nums:
            curr_sum += i
            if i > curr_sum:
                curr_sum = i
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    