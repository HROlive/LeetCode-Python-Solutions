'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        if numRows == 0:
            return pascal
        
        pascal.append([1])
        
        for row_num in range(1, numRows):
            line = [0 for i in range(row_num+1)]
            line[0] = line[-1] = 1
            pascal.append(line)
        
        if numRows > 2:
            for line in range(2, numRows):
                for ele in range(1, line):
                    pascal[line][ele] = pascal[line-1][ele-1] + pascal[line-1][ele]
                
        return pascal
