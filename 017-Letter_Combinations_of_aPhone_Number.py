'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return ''
        
        key_map = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}
        
        string_list = [key_map.get(digit) for digit in digits]
            
        all_comb = ['']
        
        for digit_letters in string_list:
            curr_comb = []
            for letter in digit_letters:
                for comb in all_comb:
                    curr_comb.append(comb + letter)
            all_comb = curr_comb
        
        return all_comb
