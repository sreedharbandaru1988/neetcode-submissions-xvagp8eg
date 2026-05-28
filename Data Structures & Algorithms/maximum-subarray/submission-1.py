class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for i in range(len(nums)):
            currentSum = 0
            for j in range(i, len(nums)):
                currentSum += nums[j]
                maxSum = max(currentSum, maxSum)
        return maxSum