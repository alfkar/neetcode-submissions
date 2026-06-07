class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,1
        counts = {s[l]:1}
        max_valid = 0
        max_key=(s[l],1)
        while r < len(s):
            length=r-l+1
            if s[r] in counts:
                counts[s[r]]+=1
            else:
                counts[s[r]]=1
            if(length>counts[max_key[0]]+k):
                counts[s[l]]-=1
                l+=1
            if max_key[1] <= counts[s[r]]:
                max_key = tuple((s[r],counts[s[r]]))
            r+=1
        overflow=max_key[1]+k-len(s)
        if overflow < 0:
            return max_key[1]+k
        else:
            return max_key[1]+k-overflow