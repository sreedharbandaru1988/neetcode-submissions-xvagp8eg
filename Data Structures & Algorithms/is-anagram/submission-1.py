class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringS = {}
        stringT = {}
        for i in s:
            stringS[i] = stringS.get(i ,0) + 1
        for j in t:
            stringT[j] = stringT.get(j ,0) + 1
        return stringS == stringT
        