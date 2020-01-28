'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]




class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_comb = []
        right_steps = m-1
        down_steps = n-1
        
        self.step(right_steps, down_steps, total_comb)
        return len(total_comb)
        
    def step(self, right_steps, down_steps, total_comb):
        if right_steps == down_steps == 0:
            total_comb += [0] # or .append(0)
            return
        
        if right_steps > 0:
            self.step(right_steps-1, down_steps, total_comb)
        if down_steps > 0:
            self.step(right_steps, down_steps-1, total_comb)
            
    
    
class Solution:
    def __init__(self):
        self.total_comb = 0
        
    def uniquePaths(self, m: int, n: int) -> int:
        right_steps = m-1
        down_steps = n-1
        
        self.step(right_steps, down_steps, self.total_comb)
        return self.total_comb
        
    def step(self, right_steps, down_steps, total_comb):
        if right_steps == down_steps == 0:
            self.total_comb += 1
        
        if right_steps > 0:
            self.step(right_steps-1, down_steps, self.total_comb)
        if down_steps > 0:
            self.step(right_steps, down_steps-1, total_comb)
            
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        right_steps = m - 1
        down_steps = n - 1
        
        curr_comb = (right_steps, down_steps)
        total_comb = [(right_steps, down_steps)]
        
        for _ in range(right_steps+down_steps):
            curr = []
            for right, down in total_comb:
                if right:
                    curr.append((right-1, down))
                if down:
                    curr.append((right, down-1))
            total_comb = curr
            
        return len(total_comb)
