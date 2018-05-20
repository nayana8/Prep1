class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        h = {}
        for x in A:
            h[x] = 0
        
        maxL = 0
        for x in A:
            if h[x] == 0:
                h[x] = 1
                l = h.get(x-1, 0)
                r = h.get(x+1, 0)
                temp = 1 + l + r
                maxL = max(temp, maxL)
                h[x-l] = temp
                h[x+r] = temp
  
                
        return maxL
