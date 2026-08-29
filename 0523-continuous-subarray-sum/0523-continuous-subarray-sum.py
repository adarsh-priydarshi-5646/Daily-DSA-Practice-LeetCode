class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        hash_map = {0: -1}
        for i in range(len(nums)):
            s += nums[i]
            rem = s % k
            if rem in hash_map:
                if (i - hash_map[rem]) >= 2:
                    return True
            else:
                hash_map[rem] = i  
        return False

       
        # for i in range(len(nums)):
        #     s = 0
        #     c = 0
        #     for j in range(i, len(nums)):
        #         s += nums[j]
        #         c += 1
        #         if c >= 2 and s%k == 0:
        #             return True
        # return False

        