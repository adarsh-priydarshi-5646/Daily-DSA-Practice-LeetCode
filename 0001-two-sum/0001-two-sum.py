class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = sorted(nums)
        leftpoint = 0
        rightpoint = len(arr)-1
        while leftpoint < rightpoint:
            su_m = arr[leftpoint] + arr[rightpoint]
            if su_m == target:
                a,b = arr[leftpoint],arr[rightpoint]
                break
            if su_m < target:
                leftpoint+=1
            else:
                rightpoint-=1
        result=[]
        if a != b:
            result.append(nums.index(a))
            result.append(nums.index(b))
            return sorted(result)
        else:
            first_index = nums.index(a)
            second_index = nums.index(b, first_index + 1)
            result.append(first_index)
            result.append(second_index)
            return result