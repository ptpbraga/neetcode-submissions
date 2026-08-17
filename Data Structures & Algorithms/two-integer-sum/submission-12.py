class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indice, numero in enumerate(nums[::-1]):
            dif = target - nums[::-1][indice]
            if dif in nums:
                j = nums.index(dif)
                ret = [j, len(nums) - indice - 1]
                return ret;