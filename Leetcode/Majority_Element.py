class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        for val in nums:
            #freq = {} is a dictionary
            #freq.get(val, 0) means find val in the dict freq 
            #so if val exists then return the current count
            #if it doesn't exists then return default as zero 
            #then adds one becoz we just saw the val again
            #freq[val] stores the updated count back to the dictionary
            freq[val] = freq.get(val, 0) + 1
            if freq[val] > n // 2:
                return val
