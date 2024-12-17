class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos = []
        neg = []
        for i in nums:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)
        
        res = []
        j = 0
        while j < len(pos):
            res.append(pos[j])
            res.append(neg[j])
            j += 1
        
        return res