class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        res = 0
        start = 0
        hash_s = {}
        for i, ch in enumerate(A,0):
            if ch in hash_s and start <= hash_s[ch]:
                start = hash_s[ch] + 1
            else:
                res = max(res, i - start + 1)
            hash_s[ch] = i
        return res