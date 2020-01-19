'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        nums.sort()
        result = []
        target = 0
        
        while target < len_nums - 2:
            if target > 0 and nums[target] == nums[target-1]:
                target += 1
                continue
            left = target + 1
            right = len_nums - 1
            
            while left < right:
                curr_sum = nums[target] + nums[left] + nums[right]
                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([nums[target], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1         
            target += 1
                
        return result
        
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
            
        result = []
        if num_count.get(0) and num_count[0] >= 3:
            result.append([0, 0, 0])
            
        neg = []
        pos = []
        for num in num_count.keys():
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        neg.sort()
        pos.sort()
        # neg = sorted(filter(lambda x: x<0, num_count.keys()))
        # pos = sorted(filter(lambda x: x>=0, num_count.keys()))
        
        for i in pos:
            for j in neg:
                k = -i -j
                new = [i, j, k]
                if k in (i, j) and num_count[k] >= 2:
                    result.append(new)
                if k in num_count.keys() and (k>i or j<k<0):
                    result.append(new)
        
        return result

    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        if len_nums < 3:
            return []
        
        solution = []
        num1 = 0
        while num1 < len_nums-2:
            num2 = num1 + 1
            while num2 < len_nums-1:
                num3 = num2 + 1
                while num3 < len_nums:
                    curr = nums[num1] + nums[num2] + nums[num3]
                    if (curr) == 0:
                        solution.append(sorted([nums[num1], nums[num2], nums[num3]]))
                    num3 += 1
                num2 += 1
            num1 += 1
            
        final_solution = []
        for i in solution:
            if i not in final_solution:
                final_solution.append(i)
                
        return final_solution
