class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalStr = s.replace(" ","")
        clean = "".join(ch.lower() for ch in s if ch.isalnum())
        length = len(clean)
        for i in range(len(clean)):
            if clean[i] == clean[length-1]:
                length -= 1
            else:
                return False
        return True