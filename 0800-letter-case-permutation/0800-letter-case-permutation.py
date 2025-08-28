class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def backtracking(index, path):
            if index == len(s):
                result.append(path)
                return
            
            ch = s[index]

            if ch.isdigit():
                backtracking(index + 1, path + ch)
            else:
                backtracking(index + 1, path + ch.lower())
                backtracking(index + 1, path + ch.upper())
            
        backtracking(0,"")
        return result