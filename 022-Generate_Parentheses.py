'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bfs = [(0, 0, '')]
        
        for _ in range(n*2):
            curr = []
            for left, right, string in bfs:
                if left+1 <= n:
                    curr.append((left+1, right, string + '('))
                if left > right:
                    curr.append((left, right+1, string + ')'))
            bfs = curr
            
        return [combination for left, right, combination in bfs]
    
    
    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        left = right = n
        self.dfs(left, right, '', result)
        
        return result
    
    def dfs(self, left, right, string, result):
        if right < left:
            return
        if not left and not right:
            result.append(string)
            return
        if left:
            self.dfs(left-1, right, string + '(', result)
        if right:
            self.dfs(left, right-1, string + ')', result)



class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(res, n, n)
        return res
    
    def helper(self, res, Open, Close, curr=''):
        if Open == 0 and Close == 0: res.append(curr)
        if Open < 0 or Close < 0: return
        
        if Open == Close:
            self.helper(res, Open-1, Close, curr+'(')

        if Open < Close:
            self.helper(res, Open-1, Close, curr+'(')
            self.helper(res, Open, Close-1, curr+')')
