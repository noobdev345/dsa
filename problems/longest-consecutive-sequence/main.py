class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        st = set(nums)
        max_count = 0
        
        for i in range(len(nums)):

            # check if current element is the starting of a sequence
            # if nums[i] - 1 not in set, means it is the starting of a sequence
            # after that keep adding 1 and check in set
            if nums[i] - 1 not in st:
                x = 1
                while nums[i] + x in st:
                    x += 1
                max_count = max(max_count, x)
        
        return max_count
