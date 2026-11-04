from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def counter(word):
            hash = {}
            for letter in word:
                hash[letter] = hash.get(letter, 0) + 1
            return hash
        
        hash = defaultdict(list)

        for word in strs:
            counts = counter(word)
            # hash[counts].append(word)
            hash[tuple(sorted(counts.items()))].append(word)
        
        arr = []
        for groups in hash.values():
            arr.append(groups)

        return arr
