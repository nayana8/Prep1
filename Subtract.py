class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        l = 0
        temp = A
        while temp != None:
            l += 1
            temp = temp.next
            
        move = l/2
        if l % 2 != 0:
            move += 1

        nextP = A
        i = 0
        st = []
        while i != move:
            nextP = nextP.next
            i += 1
        while nextP != None:
            st.append(nextP.val)
            nextP = nextP.next
     
        res = A
        i = 0
        for i in range(len(st)-1, -1, -1): 
            res.val = st[i] - res.val
            res = res.next
        return A