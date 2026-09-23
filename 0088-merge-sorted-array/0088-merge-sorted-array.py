class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1 = 0
        index2 = 0
        merge = []
        while index1 < m and index2 < n:
            if nums1[index1] < nums2[index2]:
                merge.append(nums1[index1])
                index1 += 1
            else:
                merge.append(nums2[index2])
                index2 += 1
        while index1 < m:
            merge.append(nums1[index1])
            index1 += 1
        while index2 < n:
            merge.append(nums2[index2])
            index2 += 1

        nums1[:m+n] = merge
        return nums1


