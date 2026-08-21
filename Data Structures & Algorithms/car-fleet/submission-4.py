class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort cars by position in descending order (furthest car first)
        pairs = sorted(zip(position, speed), reverse=True)

        # Calculate time to reach the target for each car (time = (target - position) / speed)
        times_to_target = [(target - pos) / spd for pos, spd in pairs]

        # Combine position, speed, and time to target for clarity
        cars_with_times = list(zip(pairs, times_to_target))  # [(position, speed), time_to_target]

        # print(cars_with_times)

        fleets = 0  # Count fleets
        prev_time = 0  # Track the time of the previous fleet

        # Traverse cars in sorted order by position (already sorted)
        for _, time in cars_with_times:
            # If current car's time to target is greater than or equal to the previous, it's in the same fleet
            if time > prev_time:
                fleets += 1  # New fleet
                prev_time = time  # Update the time for the fleet

        return fleets
