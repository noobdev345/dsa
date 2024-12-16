class Solution:
    def second_largest(self, arr):
        large, second_large = -1e9, -1e9

        for i in arr:
            if i > large:
                second_large = large
                large = i
            elif i > second_large and i != large:
                second_large = i
        
        return second_large
