class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = {}
        c2 = {}
        if len(s) != len(t):
            return False
        for l1, l2 in zip(s, t):
            if l1 not in c1:
                c1[l1] = 1
            else:
                c1[l1] += 1
            if l2 not in c2:
                c2[l2] = 1
            else:
                c2[l2] += 1
        print(c1, c2)
        if c1 == c2:
            return True
        return False
            
            
        