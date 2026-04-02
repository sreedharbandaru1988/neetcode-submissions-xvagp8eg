class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currentMax, currentMin = 0,0
        globalMax, globalMin = nums[0], nums[0]
        total = 0

        for i in nums:
            currentMax = max(currentMax + i, i)
            currentMin = min(currentMin + i, i)
            total += i
            globalMax = max(globalMax, currentMax)
            globalMin = min(globalMin, currentMin)

        return max(globalMax, total-globalMin) if globalMax>0 else globalMax