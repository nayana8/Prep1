class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        if len(A) == 0:
            return []
        res = []
        h = {}
            
        for i in range(0, len(A)):
            val = A[i]
            temp = B - val
            if temp in h:
                res.append(h[temp]+1)
                res.append(i+1)
                break
            else:
                if val in h:
                    continue
                h[val] = i
        return res