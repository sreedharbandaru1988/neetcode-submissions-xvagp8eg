class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringS = {}
        stringT = {}
        for str in s:
            stringS[str] = 1 + stringS.get(str, 0) 
        for str1 in t:
            stringT[str1] = 1 + stringT.get(str1, 0) 
        return stringS == stringT
        