class Solution:

    def is_anagram(self, s, t):

        if len(s) != len(t):
            return False

        chars_s = defaultdict(int)
        chars_t = defaultdict(int)

        for char in s:
            chars_s[char] += 1

        for char in t:
            chars_t[char] += 1

        # return chars_s == chars_t
        return all([chars_t[char_s] == value_s for char_s, value_s in chars_s.items()])

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        visited = [False] * len(strs)

        for i in range(len(strs)):
            if visited[i]:
                continue

            i_anagrams = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):
                if self.is_anagram(strs[i], strs[j]):
                    i_anagrams.append(strs[j])
                    visited[j] = True

            ans.append(i_anagrams)

        return ans
