'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle) if len(needle) != 0 else 0

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle == '':
            return 0

        n = len(needle)
        
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:
                return i

        return -1
