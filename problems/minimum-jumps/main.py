class Solution:
    def minJumps(self, arr):
        if len(arr) == 1:
            return 0

        if arr[0] == 0:
            return -1
        
        jumps = 1
        max_reach = arr[0]
        step_end = arr[0]

        for i in range(1, len(arr)):
            if i == len(arr) - 1:
                return jumps

            max_reach = max(max_reach, i + arr[i])

            if i == step_end:
                step_end = max_reach
                jumps += 1

                if step_end >= len(arr) - 1:
                    return jumps
            
            if i >= max_reach:
                return -1
        
        return -1
    