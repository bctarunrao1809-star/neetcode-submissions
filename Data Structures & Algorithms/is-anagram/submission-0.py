class Solution:
    def isAnagram(self, s, t) -> bool:
        if len(s) == len(t) and sorted(s)==sorted(t):
            return True
        else:
            return False   