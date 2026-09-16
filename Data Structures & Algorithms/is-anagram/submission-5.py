class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}
        for i in s:
            str1[i] = str1.get(i,0) + 1
        for j in t:
            str2[j] = str2.get(j,0) + 1
        return str1 == str2 
        