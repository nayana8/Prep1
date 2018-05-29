class Solution:
    # @param A : string
    # @return string
        
    def reverseWords(self, A):
        if len(A) <= 1:
            return A
            
        spaces = 0
        for ch in A:
            if ch == ' ':
                spaces += 1
        
        if spaces == 0:
            return A
            
        words = []
        words = A.split()
        A = ""
        for i in range(len(words)-1, -1, -1):
            if len(A) > 0:
                A += " "
            A += words[i]
        return A