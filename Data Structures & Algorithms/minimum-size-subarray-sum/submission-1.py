class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = 0
        L = 0
        length = float("inf")

        for R in range(len(nums)):
            current_sum += nums[R]
            while current_sum >= target:
                length = min(R-L+1, length)
                current_sum -= nums[L]
                L += 1
        return 0 if length == float("inf") else length

        