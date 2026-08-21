class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            target_pair = target - num

            if target_pair in h:
                return h[target_pair], i
            else:
                h[num] = i
