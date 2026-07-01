class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        testset = set()
        for item in nums:
            if item in testset:
                return True
            testset.add(item)
        return False