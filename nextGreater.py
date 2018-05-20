class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        st = []
        res = {}
        if len(A) == 0:
            return st
        if len(A) == 1:
            st.append(-1)
            return st
            
        st.append(0)
        for i in xrange(1, len(A)):
            next = A[i]
            
            if len(st) != 0:
                elem = st.pop()
                
                while A[elem] < next:
                    res[elem] = next
                    if len(st) == 0:
                        break
                    elem = st.pop()
                    
                if A[elem] >= next:
                    st.append(elem)
                    
            st.append(i)

		while len(st) != 0:
            elem = st.pop()
            next = -1
            res[elem] = next
            
        rt = []
        for i in xrange(len(A)):
            if i in res:
                rt.append(res[i])
            else:
                rt.append(-1)
        return rt