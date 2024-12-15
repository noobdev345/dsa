import math

class Solution:
    def check_armstrong(num):
        num_of_digits = math.floor(math.log10(num)) + 1
        
        total = 0
        temp = num
        while temp:
            r = temp % 10
            total += r ** num_of_digits
            temp //= 10
        
        return total == num
    