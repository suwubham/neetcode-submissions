class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1, c2 = {}, {}
        for l1, l2 in zip(s, t):
            c1[l1] = c1.get(l1, 0) + 1
            c2[l2] = c2.get(l2, 0) + 1
        return c1 == c2
            
            
        