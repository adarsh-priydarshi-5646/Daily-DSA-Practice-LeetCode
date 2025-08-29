class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrac(start,path):
            res.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrac(i + 1, path)
                path.pop()
        
        backtrac(0,[])
        return res

        