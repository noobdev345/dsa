class Solution:
    def evenlyDivides(self, n):
        count = 0
        temp = n
        while temp:
            r = temp % 10
            if r != 0 and n % r == 0:
                count += 1
            temp //= 10
        return count
