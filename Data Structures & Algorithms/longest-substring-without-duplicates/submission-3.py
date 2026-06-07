class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0,1
        sub_string={s[l]}
        max_len=len(sub_string)
        while r < len(s):
            if s[r] not in sub_string:
                sub_string.add(s[r])
                max_len=max(max_len,len(sub_string))
                r+=1
            else:
                sub_string.remove(s[l])
                l+=1
        return max_len