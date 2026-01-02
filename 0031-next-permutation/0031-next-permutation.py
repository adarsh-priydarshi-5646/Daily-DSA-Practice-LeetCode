class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        if pivot == -1:
            nums.reverse()
            return
        arr1 = nums[:pivot]
        arr2 = nums[pivot:]

        for i in range(len(arr2) - 1, 0, -1):
            if arr2[i] > arr2[0]:
                arr2[0], arr2[i] = arr2[i], arr2[0]
                break

        arr2[1:] = sorted(arr2[1:])
        nums[:] = arr1 + arr2
