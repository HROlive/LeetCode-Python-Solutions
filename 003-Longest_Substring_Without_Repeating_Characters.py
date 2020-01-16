'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        curr_str = ''
        
        for char in s:
            if char not in curr_str:
                curr_str += char
            else:
                max_len = max(max_len, len(curr_str))
                duplicated_char_idx = curr_str.find(char)
                curr_str = curr_str[duplicated_char_idx+1:] + char
                
        return max(max_len, len(curr_str))
