class Solution:
    def leaders(self, arr):
        res = []
        maxi = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1 or arr[i] >= maxi:
                maxi = arr[i]
                res.append(arr[i])
        
        res = res[::-1]
        return res
    