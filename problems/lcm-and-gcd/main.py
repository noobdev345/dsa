class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        lcm = (a // gcd(a, b)) * b
        
        res = [lcm, gcd(a, b)]
        
        return res
    