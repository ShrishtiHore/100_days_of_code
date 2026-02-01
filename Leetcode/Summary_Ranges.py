class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        n = len(nums)
        
        #to handle an empty input
        if n == 0:
            return result

        #start the range
        start = nums[0]
        
        #move from left to right one element at a time
        for i in range(1, n):
            if nums[i] != nums[i - 1] + 1: #check if the elements are consecutive
                
                # range ended
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        # handle last range
        #The loop ends without closing the last range, so we must do it manually.
        #This handles: 1.single last number [or] last multi-number range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")

        return result
