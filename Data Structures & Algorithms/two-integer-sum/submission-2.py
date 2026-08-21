class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {} # {num:idx}
        for idx, num in enumerate(nums):
            remainder = target - num
            if remainder in h:
                return [h[remainder], idx, ]
            h[num] = idx
            
            

        