class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)
        actual_sum = n * (n + 1) // 2
        return actual_sum - total
    