class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        new = []

        for val in nums:
            if val != 0:
                new.append(val)
        
        zeros = [0] * (len(nums) - len(new)) #multiply zero with total - non zero 
        nums[:] = new + zeros
