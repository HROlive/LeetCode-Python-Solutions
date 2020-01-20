'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        traveler = n_node = head
        # n_node = head
        node_num = 1
        
        while traveler.next:
            if node_num <= n:
                traveler = traveler.next
                node_num += 1          
            else:
                traveler = traveler.next
                n_node = n_node.next
                      
        if node_num == n:
            return head.next
        else:
            # much faster if we uncomment bellow. why?
            # clear_node = n_node.next
            n_node.next = n_node.next.next
            # clear_node.next = None
            return head
