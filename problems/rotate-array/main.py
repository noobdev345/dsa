class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        
        def reverse(arr, left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            return arr
        
        k %= len(nums)

        nums = reverse(nums, 0, len(nums) - 1)
        nums = reverse(nums, 0, k - 1)
        nums = reverse(nums, k, len(nums) - 1)
        