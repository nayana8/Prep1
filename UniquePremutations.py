class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, nums):
        def insert_num(temp, num):
            if temp == []:
                temp.append([num])
                return temp

            res = []
            for i in temp:
                for j in range(len(i) + 1):
                    i_copy = list(i)
                    i_copy.insert(j, num)
                    res.append(i_copy)
            return res

        temp = []
        for i in nums:
            temp = insert_num(temp, i)  
        temp = sorted(temp)
        res = [temp[i] for i in range(len(temp)) if i == 0 or temp[i] != temp[i-1]]
        return res