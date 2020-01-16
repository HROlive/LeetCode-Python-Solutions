'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ''
        
        for i in range(len(s)):
            even = self.palindromeFromCenter(s, i, i+1)
            odd = self.palindromeFromCenter(s, i, i)
            
            curr_palindrome = even if len(even)>len(odd) else odd
            max_palindrome = max_palindrome if len(max_palindrome)>len(curr_palindrome) else curr_palindrome
        
        return max_palindrome
            
    def palindromeFromCenter(self, string, left_start_idx, right_start_idx):
        left_final_idx = 0
        right_final_idx = 0
        
        while left_start_idx >= 0 and right_start_idx < len(string):
            if string[left_start_idx] == string[right_start_idx]:
                left_final_idx = left_start_idx
                right_final_idx = right_start_idx
            else:
                break
            left_start_idx -= 1
            right_start_idx += 1
            
        return string[left_final_idx:right_final_idx+1]
        
