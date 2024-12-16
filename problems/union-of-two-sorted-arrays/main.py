class Solution:
    def union(arr1: list[int], arr2: list[int]) -> list[int]:
        res = []

        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            
            if arr1[i] <= arr2[j]:
                if len(res) == 0 or res[-1] != arr1[i]:
                    res.append(arr1[i])
                    i += 1
            else:
                if len(res) == 0 or res[-1] != arr2[j]:
                    res.append(arr2[j])
                    j += 1
        
        while i < len(arr1):
            if res[-1] != arr1[i]:
                res.append(arr1[i])
                i += 1
        
        while j < len(arr2):
            if res[-1] != arr2[j]:
                res.append(arr2[j])
                j += 1
        
        return res
        
