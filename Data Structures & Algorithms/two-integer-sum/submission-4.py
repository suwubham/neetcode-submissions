class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for idx, num in enumerate(nums):
            if num in map:
                return [map.get(num), idx]
            complement = target - num
            map[complement] = idx 
        