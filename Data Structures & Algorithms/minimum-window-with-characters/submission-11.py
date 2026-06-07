from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len (t):
            return ""
        ct = Counter(t)
        left = 0
        minimum_valid = ""
        substr = s[left]
        for right in range(len(s)):
            substr = substr + s[right]
            while (not (ct - Counter(substr))):
                if minimum_valid == "" or len(substr) < len(minimum_valid):
                    minimum_valid = substr
                left = left + 1
                substr = substr[1:]
        return minimum_valid
