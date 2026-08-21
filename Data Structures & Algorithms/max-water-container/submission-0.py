"""
height = [1,7,2,5,4,7,3,6]
          L(0)
                        R(7)
min_height = 1
max_area = 1 * 8 = 8
"""

class Solution:
    # T: O(2N) -> O(N), S: O(1)
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0
        left, right = 0, len(heights) - 1

        while left < right:
            # calculate the max area based on the min height * width
            width = right - left
            min_height = min(heights[left], heights[right]) 
            area = min_height * width
            max_area = max(max_area, area)
            
            # move pointers where height is less
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_area
