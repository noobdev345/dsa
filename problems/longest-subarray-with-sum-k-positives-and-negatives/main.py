class Solution:
    def lenOfLongestSubarr(self, arr, k):  
        prefix_sum_map = {}
        s = 0
        res = 0
        
        for i in range(len(arr)):
            s += arr[i]
            
            if s == k:
                res = max(res, i + 1) # for 1-based indexing
            
            rem = s - k
            if rem in prefix_sum_map:
                dist = i - prefix_sum_map[rem]
                res = max(res, dist)
            
            if s not in prefix_sum_map:
                prefix_sum_map[s] = i
        
        return res
    