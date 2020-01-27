'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_keys = {}
        
        for word in strs:
            sorted_word = tuple(sorted(word))
            sorted_keys[sorted_word] = sorted_keys.get(sorted_word, []) + [word]
            
            # or
            # sorted_word = ''.join(sorted(word))
            # sorted_keys[sorted_word] = sorted_keys.get(sorted_word,[]) + [word]
            
            # or
            # sorted_word = ''.join(sorted(word))
            # if sorted_word in sorted_keys.keys():
            #     sorted_keys[sorted_word] = sorted_keys[sorted_word] + [word]
            # else:
            #     sorted_keys[sorted_word] = [word]
                
        return sorted_keys.values()
