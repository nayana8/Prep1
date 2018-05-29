class Solution:
    # @param A : tuple of integers
    # @return an integer
    def setBit(self, num, x):
        if num == 0:
            return False
        return (num >> x) & 1
        
    def repeatedNumber(self, A):
        temp = 0
        res = 0
        for x in A:
            temp = 1 << x
            if self.setBit(res, x):
                return x
            res = res | temp
        return -1