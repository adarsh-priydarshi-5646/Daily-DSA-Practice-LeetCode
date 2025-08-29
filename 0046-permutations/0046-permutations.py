class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def back(path,check):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if not check[i]:
                    check[i] = True
                    path.append(nums[i])
                    back(path,check)
                    path.pop()
                    check[i] = False
        
        back([],[False]*len(nums))
        return res