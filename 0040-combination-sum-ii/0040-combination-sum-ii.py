class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to handle duplicates
        res = []

        def backtrack(start, path, curr_sum):
            if curr_sum == target:
                res.append(path)
                return
            if curr_sum > target:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                backtrack(i + 1, path + [candidates[i]], curr_sum + candidates[i])
        
        backtrack(0, [], 0)
        return res
            