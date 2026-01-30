#sort the array
#check for first element if its equal to next
#check for last element if its equal to previous
#check for previous element if its equal to left and then check for right
#if in any of these cases the number is not equal then its unique

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) > 1:
            for i in range(len(nums)):
                if (i == 0 and nums[i] != nums[i+1]) or \
                   (i == len(nums)-1 and nums[i] != nums[i-1]) or \
                   (nums[i] != nums[i-1] and nums[i] != nums[i+1]):
                    return nums[i]
        else:
            return nums[0]



