class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge(arr, low, mid, high):
            cnt = 0
            # Count reverse pairs: arr[i] > 2 * arr[j]
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and arr[i] > 2 * arr[j]:
                    j += 1
                cnt += (j - (mid + 1))
            
            #merge sort
            temp = []
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
                    
            while left <= mid:
                temp.append(arr[left])
                left += 1
                
            while right <= high:
                temp.append(arr[right])
                right += 1
                
            for i in range(len(temp)):
                arr[low + i] = temp[i]
    
            return cnt

        def mergeSort(arr, low, high):
            if low >= high:
                return 0
            mid = (low + high) // 2
            cnt = mergeSort(arr, low, mid)
            cnt += mergeSort(arr, mid + 1, high)
            cnt += merge(arr, low, mid, high)
            return cnt
            
        return mergeSort(nums, 0, len(nums) - 1)