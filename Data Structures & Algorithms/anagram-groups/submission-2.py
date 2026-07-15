class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            sortedstr = "".join(sorted(str))
            if sortedstr in anagrams:
                anagrams[sortedstr].append(str)
            else:
                anagrams[sortedstr] = [str]
        return list(anagrams.values())



        