class Solution:
    def helper(self,i,j,text1,text2,memo):
        if i == 0 or j == 0:
            return 0

        if (i,j) in memo:
            return memo[(i,j)]

        if text1[i-1] == text2[j-1]:
            memo[(i,j)] = 1 + self.helper(i-1,j-1,text1,text2,memo)
        else:
            memo[(i,j)] = max(self.helper(i-1,j,text1,text2,memo),self.helper(i,j-1,text1,text2,memo))

        return memo[(i,j)]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        return self.helper(len(text1),len(text2),text1,text2,memo)
        