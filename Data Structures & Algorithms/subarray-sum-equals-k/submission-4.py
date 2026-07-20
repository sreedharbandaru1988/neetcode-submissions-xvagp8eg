class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0   
        for i in range(len(nums)):
            currentSum = nums[i]
            if currentSum == k:
                count += 1
            for j in range(i+1, len(nums)):
                currentSum += nums[j]
                if currentSum == k:
                    count += 1
        return count


