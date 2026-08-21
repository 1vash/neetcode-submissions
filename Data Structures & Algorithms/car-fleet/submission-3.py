class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(list(zip(position, speed)), reverse=True)

        slopes = [(target - pos) / speed for pos, speed in pairs]

        pairs_with_slopes = list(zip(pairs, slopes))

        print(pairs_with_slopes)

        prev_fleet_time = 0
        fleets = 0
        
        # Traverse cars in sorted order by position (already sorted)
        for _, time in pairs_with_slopes:
            # If current car's time to target is greater than or equal to the previous, it's in the same fleet
            if time > prev_fleet_time:
                fleets += 1  # New fleet
            
                prev_fleet_time = time  # Update the time for the fleet
        
        return fleets