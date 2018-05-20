import heapq

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        h = []
        i = 0
        while i < B:
            h.append(A[i])
            i += 1
        heapq.heapify(h)
        h.sort()
        while i < len(A):
            temp = h[-1]
            if temp > A[i]:
                h[-1] = A[i]
                heapq.heapify(h)
                h.sort()
            i += 1
        return h[-1]