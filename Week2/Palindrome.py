class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        n = len(A)
        if n <= 1:
            return 1
            
        i = 0
        n = n - 1
        l = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        A = A.lower()
        while i < n:
            if A[i] not in l:
                i += 1
                continue
            if A[n] not in l:
                n -= 1
                continue
            
            if A[i] != A[n]:
                return 0
            i += 1
            n -= 1
        return 1
