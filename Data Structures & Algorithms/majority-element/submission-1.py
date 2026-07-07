class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityHash = {}
        for i in nums:
            majorityHash[i] = majorityHash.get(i,0) + 1
            
        for i, j in majorityHash.items():
            if j > len(nums)/2:
                return i