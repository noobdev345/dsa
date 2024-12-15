class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647
        MIN = -2147483648

        res = 0
        temp = abs(x)
        is_neg = True if x < 0 else False

        while temp:
            res = res * 10 + (temp % 10)
            temp //= 10
        
        if res >= MAX or res <= MIN:
            res = 0
        
        return -res if is_neg else res
    