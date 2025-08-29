class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()   # Step 1: sort to group duplicates
        res = []

        def back(path, check):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if check[i]:
                    continue

                # Step 2: skip duplicates
                if i > 0 and nums[i] == nums[i-1] and not check[i-1]:
                    continue

                check[i] = True
                path.append(nums[i])
                back(path, check)
                path.pop()
                check[i] = False

        back([], [False] * len(nums))
        return res
        