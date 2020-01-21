'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        start_l = start_r = -1
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                start_l = start_r = mid
                while True:
                    if start_l-1 >= l and nums[start_l-1] == target:
                        start_l -= 1
                    elif start_r+1 <= r and nums[start_r+1] == target:
                        start_r += 1
                    else:
                        break
                return [start_l, start_r]
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
                
        return [start_l, start_r]
