class Solution:
    def sortColors(self, nums: list[int]) -> None:
        color = [0, 0, 0]
        for i in nums:
            if i == 0:
                color[0] += 1
            elif i == 1:
                color[1] += 1
            else:
                color[2] += 1
        
        j = 0
        while color[0]:
            nums[j] = 0
            j += 1
            color[0] -= 1

        while color[1]:
            nums[j] = 1
            j += 1
            color[1] -= 1
        
        while color[2]:
            nums[j] = 2
            j += 1
            color[2] -= 1
        