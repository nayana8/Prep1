class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        neg = 0
        small = 1000000
        big = -1000000
        res = 0
        h = {}
        for i in range(len(A)):
            if A[i] <= 0:
               neg += 1
            else:
                small = min(small, A[i])
                big = max(big, A[i])
                h[A[i]] = 1
                res += A[i]
            
        temp = 0    
        if small > 1:
            return 1
        for i in range(small, big+1):
            if i not in h:
                return i
        

        return big+1