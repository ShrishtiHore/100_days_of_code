class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result = []
        nums = nums1[:m] + nums2[:n] #take only the first m and n elements from nums 1 and nums2, that leaves the buffer zero elements which are placeholders not real values for merge
        for i in nums:
            if i != 0:
                result.append(i)
        result.sort()
        nums1[:] = result #this is becoz leetcode wants nums1 in result or i would have just returned result
        
