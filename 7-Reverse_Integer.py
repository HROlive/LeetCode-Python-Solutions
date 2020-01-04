'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
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
