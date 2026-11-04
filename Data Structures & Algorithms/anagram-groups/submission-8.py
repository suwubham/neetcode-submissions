from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_counts = defaultdict(list)
        
        for word in strs:
            counts = Counter(word)
            all_counts[tuple(sorted(counts.items()))].append(word)
        
        return list(all_counts.values())