from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # hash(s): List
        
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())