# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        if A == None:
            return None
            
        length = 1
        temp = A
        while temp != None:
            temp = temp.next
            length += 1
            
        mid = length / 2
        midNode = A
        i = 0
        tmep = None
        while i < mid:
            temp = midNode
            midNode = midNode.next
            i += 1
            
        if length % 2 != 0:
            temp = midNode
            midNode = midNode.next
            
        temp.next = None

        # Reverse the list from mid to end
        cur = midNode
        newHead, prev = None, None
        while cur != None:
            prev = cur.next
            cur.next = newHead
            newHead = cur
            cur = prev
            
        midNode = newHead
        start = A
        while midNode != None:
            startNext = start.next
            start.next = midNode
            midNext = midNode.next
            midNode.next = startNext
            start = startNext
            midNode = midNext
            
        return A