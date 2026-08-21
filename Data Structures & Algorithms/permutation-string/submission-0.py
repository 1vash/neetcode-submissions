class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        h_s1 = {}
        
        for s in s1:
            h_s1[s] = h_s1.get(s, 0) + 1

        print(h_s1)
        
        l = 0
        for r in range(len(s2)):

            # UPDATE only the letters related in h_s1, all others are skipped.
            
            # make sliding window borders valid and back increase 
            # `already decreased` character's counter
            while r - l + 1 > len(s1):
                if s2[l] in h_s1:
                    h_s1[s2[l]] += 1
                l += 1

            # decrease character's counter
            if s2[r] in h_s1:
                h_s1[s2[r]] -= 1
            

            # if all zeros, then we've got a valid permutation in string
            if all(v == 0 for v in h_s1.values()):
                return True

        return False 