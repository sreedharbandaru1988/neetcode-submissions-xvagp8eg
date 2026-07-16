class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        inf = float('inf')
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = inf
                count += 1
        nums.sort()
        return len(nums)-count