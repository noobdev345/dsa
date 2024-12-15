import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], x: int) -> float:
        
        def delta(p, t):
            return (p + 1) / (t + 1) - (p / t)
        
        # max heap to store a tuple of (-gain, pass, total)
        max_heap = []

        for p, t in classes:
            gain = delta(p, t)
            heapq.heappush(max_heap, (-gain, p, t))

        # distribute the students
        while x:
            curr_gain, p, t = heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-delta(p + 1, t + 1), p + 1, t + 1))
            x -= 1
        
        pass_ratio = 0
        while max_heap:
            curr_gain, p, t = heapq.heappop(max_heap)
            pass_ratio += p / t
        
        return pass_ratio / len(classes)
    