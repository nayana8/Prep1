class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        if A == 0:
            return []
        n = (A * 2) - 1
        last = n - 1
        level = A
        matrix = [[0 for i in range(0,n)] for j in range(0, n)]
        for k in range(0, level):
            for i in range(k, n):
                for j in range(i, n):
                    matrix[i][j] = A
                    matrix[j][i] = A
                    matrix[last][j] = A
                    matrix[j][last] = A
            A = A - 1
            last = last - 1
            n = n - 1
        return matrix