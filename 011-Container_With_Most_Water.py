'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_water = 0
        
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            max_water = max(max_water, w*h)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_height = max(height)
        len_height = len(height)
        set_height = set(height)
        max_area = 0
        
        for h in set_height:
            left = 0
            right = -1
            left_found = right_found = False
            while left < len_height:
                if h <= height[left]:
                    left_found = True
                    break
                left += 1
            
            if left_found:
                while (len_height + right) > left:
                    if h <= height[right]:
                        right_found = True
                        break
                    right -= 1
            
            if left_found and right_found:
                w = (len_height+right) - left
                max_area = max(w*h, max_area)
        
        return max_area
