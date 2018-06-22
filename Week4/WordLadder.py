class Solution:
    
    def getNeigh(self, word, dictV):
        child = []
        for w in dictV:
            counter = 0
            if len(w) != len(word):
                continue
            for i in range(len(word)):
                if word[i] != w[i]:
                    counter += 1
            if counter == 1:
                child.append(w)
                
        return child
        
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        if start == end:
            return 1
            
        dictV.append(end)
        visited = {}
        q = []
        q.append((start,0))
        while len(q) > 0:
            s = q.pop(0)[0]
            if s in visited:
                continue

            visited[s] = True
            neigh = self.getNeigh(s, dictV)
            #print s, neigh
            if len(neigh) == 0:
                break
            for n in neigh:
                if n == end:
                    print s[1]
                    return 0
                q.append((n,s[1]+1))
        return 0