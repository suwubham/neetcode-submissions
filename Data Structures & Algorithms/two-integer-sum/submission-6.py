class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map.get(complement), idx]
            map[num] = idx