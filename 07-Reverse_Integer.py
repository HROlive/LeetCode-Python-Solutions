'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x_list = list(str(x))
            x_list_reversed = x_list[:0:-1]
            x_reversed = "-" + "".join(x_list_reversed)
            x_reversed = int(x_reversed)
        else:
            x_list = list(str(x))
            x_list_reversed = x_list[::-1]
            x_reversed = int("".join(x_list_reversed))
        
        return x_reversed if -2**31 < x_reversed < 2**31-1 else 0
