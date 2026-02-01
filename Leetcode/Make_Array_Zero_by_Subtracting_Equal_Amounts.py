class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        positives = []

        for num in nums:
            if num > 0:
                positives.append(num)

        unique_values = set(positives)
        return len(unique_values)
