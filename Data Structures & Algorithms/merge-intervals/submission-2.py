class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # T: O nlogn; S: O(N) for the output
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        
        for start_2, end_2 in intervals[1:]:
            start_1, end_1 = merged[-1]

            if start_2 <= end_1:
                merged[-1] = [min(start_1, start_2), max(end_1, end_2)]
            else:
                merged.append([start_2, end_2])

        return merged