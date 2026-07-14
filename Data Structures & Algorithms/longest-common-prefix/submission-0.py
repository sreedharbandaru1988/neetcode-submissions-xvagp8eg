class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        
        for i in range(len(strs)):
            char1 = strs[0][i]
            count = 0
            for j in range(len(strs)-1):
                if char1 == strs[j+1][i]:
                    count += 1
            if count == len(strs) - 1:
                result = result + char1
            else:
                break
        return result
                
        