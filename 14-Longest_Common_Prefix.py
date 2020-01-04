'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        equal = True
        letter_count = 0
        
        if len(strs) < 1:
            return prefix
        
        elif len(strs) == 1:
            return strs[0]
        
        else:        
            while equal:
                letter_set = set()
                
                for word in strs:
                    if len(word) == 0 or letter_count > len(word)-1:
                        return prefix
                    letter = word[letter_count]
                    letter_set.add(letter)
                    
                if len(letter_set) == 1:
                    prefix += letter
                    letter_count += 1
                    
                else:
                    equal = False

            return prefix
                
