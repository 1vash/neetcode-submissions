class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # T: O(m nlogn ~ 100); S O(m*n~100) -> not optimized
        h = defaultdict(list) # sorted(s): List
        for s in strs:
            # len(s) <= 100 
            h["".join(sorted(s))].append(s)
        return list(h.values())
