class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t) and Counter(s) == Counter(t):
            return True
        else:
            return False
        