from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sorted_counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)[:k]
        return [
            num for num, count in sorted_counts
        ]
        
        