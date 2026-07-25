class Solution:
    def countSubstrings(self, s: str) -> int:
        
        s = list(s.lower())
        count = 0
        seen = []

        for i in range(len(s)):
            j = 1
            while j <= len(s) - i:
                piece = s[i:i+j]
                if piece in seen:
                    j += 1
                    pass
                elif piece == piece[::-1]:
                    j += 1
                    count += 1
                else:
                    j += 1
                    pass

        return count
        