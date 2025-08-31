class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: sort to group duplicates
        result = []
        n = len(nums)

        def dfs(index, subset):
            # Add current subset
            result.append(subset[:])

            # Explore choices
            for i in range(index, n):
                # Skip duplicate
                if i > index and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                dfs(i + 1, subset)
                subset.pop()  # backtrack
        
        dfs(0, [])
        return result
        