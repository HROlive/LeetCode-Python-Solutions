'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_comb = [[]]
        len_nums = len(nums)
        
        for _ in range(len_nums):
            curr = []
            for comb in all_comb:
                for num in nums:
                    if num not in comb:
                        curr.append(comb + [num])
            all_comb = curr
            
        return all_comb
    
    
# class Solution:
#     def permute(self, nums):
#         res = []
#         self.dfs(nums, [], res)
#         return res

#     def dfs(self, nums, path, res):
#         if not nums:
#             res.append(path)
#             # return # backtracking
#         for i in range(len(nums)):
#             self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        
        
# class Solution:
#     def permute(self, nums):
#         perms = [[]]   
#         for n in nums:
#             new_perms = []
#             for perm in perms:
#                 for i in range(len(perm)+1):   
#                     new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
#             perms = new_perms
#         return perms
