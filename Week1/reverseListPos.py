# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        temp = 1
        prevStart = None
        start = A
        nextEnd = None
        end = None
        
        if B == C:
            return A
            
        while temp != B:
            prevStart = start
            start = start.next
            temp += 1
        
        end = start
        while temp != C:
            end = end.next
            temp += 1
        nextEnd = end.next
        end.next = None

        #print end.val, start.val
        newHead, cur = None, None
        while start != None:
            cur = start.next
            start.next = newHead
            newHead = start
            start = cur

        if prevStart == None:
            A = newHead
        else:
            prevStart.next = newHead
            
        while newHead.next != None:
            newHead = newHead.next
        newHead.next = nextEnd
        
        return A