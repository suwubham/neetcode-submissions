class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement not in hash:
                hash[num] = index
            else:
                return [hash[complement], index]
        return "Not found"