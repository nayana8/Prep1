class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        if len(A) == 0:
            return 0
            
        st = []
        res = 0
        st.append(-1)
        for i in range(0,len(A)):
            if A[i] == '(':
                st.append(i)
            else:
                st.pop()
                if len(st) > 0:
                    res = max(res, i - st[len(st)-1])
                else:
                    st.append(i)
        return res