class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        current_sum = 0
        prefix_sums = {0: 1}
        for i in range(n):
            current_sum += nums[i]
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        return count

        # n = len(nums) 
        # cnt = 0
        # for i in range(n):
        #     currentSum = 0
        #     for j in range(i, n):
        #         currentSum += nums[j]
        #         if currentSum == k:
        #             cnt += 1
        # return cnt
