class Solution:
    def trap(self, height: List[int]) -> int:
        # T: O(N), S: O(N)
        # formula: min(max(left, max(right)) - curr_height

        prefix_max = [None] * len(height)
        cum_max = 0 
        for i in range(len(height)):
            cum_max = max(height[i], cum_max)
            prefix_max[i] = cum_max

        postfix_max = [None] * len(height)
        cum_max = 0 
        for i in range(len(height)-1, -1, -1):
            cum_max = max(height[i], cum_max)
            postfix_max[i] = cum_max

        # print('Prefix:', prefix_max)
        # print('Postfix:', postfix_max)

        total_water = 0
        # Iterate over trapping water heights, excluding first/last boundaries as they have no water
        for i in range(1, len(height)-1): # O(N)

            left_max_height = prefix_max[i-1]
            right_max_height = postfix_max[i+1]

            cell_water = min(left_max_height, right_max_height) - height[i] 

            # print(f"Cell: {i}, Left Max {left_max_height}, Right Max {right_max_height}, Water {cell_water}")
            
            # append water, avoid negative sums-up
            total_water += 0 if cell_water < 0 else cell_water

        return total_water