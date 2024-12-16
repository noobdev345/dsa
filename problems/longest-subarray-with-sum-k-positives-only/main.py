def longestSubarrayWithSumK(a: list[int], k: int) -> int:
    i, j = 0, 0
    s = 0
    res = 0

    while j < len(a):
        s += a[j]

        while i < j and s > k:
            s -= a[i]
            i += 1
        
        if s == k:
            res = max(res, j - i + 1)
        j += 1
    
    return res
