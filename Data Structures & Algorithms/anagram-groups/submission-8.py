class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # T: O(m*n) where n~100; S: O(m*n~26)
        h = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count) # tuples are immutable, can use as key
            h[key].append(s)
        return list(h.values())
