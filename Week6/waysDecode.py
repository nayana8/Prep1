class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        p = A[0]
        res = [1] * len(A)
        if p == '0':
            return 0
            
        for i in range(1, len(A)):
            c = A[i]
            if p == '0' and c == '0':
                return 0
            elif p == '0' and c in list('123456789'):
                res[i] = res[i-1]
            elif p in list('12') and c == '0' and i >1:
                res[i] = res[i-2]
            elif p in list('12') and c == '0':
                res[i] = res[i-1]
            elif p in list('3456789') and c == '0':
                return 0
            elif p+c > '26':
                res[i] = res[i-1]
            else:
                res[i] = res[i-1] + res[i-2]
            p = c
            
        return res[-1]