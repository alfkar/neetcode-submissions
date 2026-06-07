class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        ct = self.init_T(t)
        left = 0
        minimum_valid = ""
        window = {}
        window[s[left]] = 1
        substr = s[left]
        for right in range(len(s)):
            if right > 0:
                window[s[right]] = window.get(s[right], 0) + 1
                substr = substr + s[right]
            while self.is_valid(ct, window):
                if minimum_valid == "" or len(substr) < len(minimum_valid):
                    minimum_valid = substr
                substr = substr[1:]
                if window[s[left]]:
                    window[s[left]] = window[s[left]] - 1
                left = left + 1
        return minimum_valid

    def init_T(self, T):
        T_map = {}
        for c in T:
            T_map[c] = T_map.get(c, 0) + 1
        return T_map

    def is_valid(self, need, window):
        for c in need:
            if window.get(c, 0) < need[c]:
                return False
        return True