from collections import defaultdict

class Solution:
    # T: O(m*n log n); S O(m*n) -> not optimized
    def groupAnagrams_1(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # sorted(s): List
        
        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)

        return list(groups.values())

    # T: O(m*n), S: O(m*26) -> O(m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # count(s): List
        
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - 97] += 1

            groups[tuple(count)].append(s)

        return list(groups.values())