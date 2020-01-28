'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        biggest_distance = 0
        distance_to_travel = len(nums) - 1
        
        if distance_to_travel <= 0:
            return True
        
        for i in range(distance_to_travel):
            if i > biggest_distance:
                return False
            
            biggest_distance = max(biggest_distance, i + nums[i])
            
            if biggest_distance >= distance_to_travel:
                return True
            


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         len_nums = len(nums)
#         if len_nums == 1:
#             return True
#         elif len_nums == 0:
#             return False
#         start_idx = 0
#         goal_idx = len_nums - 1
#         distance = goal_idx - start_idx
        
#         while start_idx < goal_idx:
#             if nums[start_idx] >= distance:
#                 if start_idx == 0:
#                     return True
#                 goal_idx = start_idx
#                 start_idx = 0
#                 distance = goal_idx - start_idx
#             else:
#                 start_idx += 1
#                 distance = goal_idx - start_idx
                
#         return False
