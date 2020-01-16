'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_int_reversed = self.linkedlist_to_invertedint(l1)
        l2_int_reversed = self.linkedlist_to_invertedint(l2)
        
        str_sum = str(l1_int_reversed + l2_int_reversed)
        
        result_head = ListNode(int(str_sum[::-1][0]))
        pointer = result_head
        
        for i in str_sum[::-1][1:]:
            node = ListNode(int(i))
            pointer.next = node
            pointer = node
        
        return result_head
    
    
    def linkedlist_to_invertedint(self, ListNode):
        space = []
        
        while ListNode is not None:
            space.append(ListNode.val)
            ListNode = ListNode.next
            
        reversed_int = int(''.join(map(str, space[::-1])))
        
        return reversed_int
        
        
class Solution2:
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next
