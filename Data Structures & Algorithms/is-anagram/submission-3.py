class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count1 = {}
        count2 = {}
        for i, j in zip(s, t):
            if i in count1:
                count1[i] += 1
            else:
                count1[i] = 1
            if j in count2:
                count2[j] += 1
            else:
                count2[j] = 1
        return count1 == count2
            
        