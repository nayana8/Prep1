# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the root node in the tree
    def getNode(self, A, mid):
        temp = A
        for i in range(0, mid):
            temp = temp.next
        return temp
            
    def sortedBst(self, A, low, high):
        if low > high:
            return None
        
        mid = (low+high)/2
        temp = self.getNode(A, mid)
        #print mid, temp.val
        root = None
        if temp != None:
            root = TreeNode(temp.val)
            root.left = self.sortedBst(A, low, mid-1)
            root.right = self.sortedBst(A, mid+1, high)
        
        return root
        
    def sortedListToBST(self, A):
        if A == None:
            return None
            
        low = 0
        high = 0
        cur = A
        while cur != None:
            high += 1
            cur = cur.next
            
        root = self.sortedBst(A, low, high)
        return root