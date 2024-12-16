class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            
            elif zero_count:
                nums[i], nums[i - zero_count] = nums[i - zero_count], nums[i]
    