# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        slow = A
        fast = A
        
        while slow != None and fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
         
        if slow != fast:
            return None
            
        cur = A
        while cur != slow:
            cur = cur.next
            slow = slow.next
            
        return cur