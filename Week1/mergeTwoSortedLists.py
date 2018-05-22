class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A == None:
            return B
        if B == None:
            return A
            
        if A.val < B.val:
            res = A
        else:
            res = B
        
        prev = None
        while A != None and B != None:
            if A.val < B.val:
                while A != None and A.val < B.val:
                    prev = A
                    A = A.next
                prev.next = B
            else:
                while B != None and A.val >= B.val:
                    prev = B
                    B = B.next
                prev.next = A
        if A != None:
            prev.next = A
        if B != None:
            prev.next = B
        return res