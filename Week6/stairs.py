class Solution:
    # @param A : integer
    # @return an integer
    def getWays(self, A, m):
        if A == 0:
            m[0] = 0
            
        if A == 1:
            m[1] = 1
            
        if A == 2:
            m[2] = 2
            
        m[A] = m[A-1] + m[A-2]
        
    def climbStairs(self, A):
        m = 
        return self.getWays(A)