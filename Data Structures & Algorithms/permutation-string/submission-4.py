class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target={}
        target_len=0
        for char in s1:
            if char in target:
                target[char] +=1
            else:
                target[char] = 1
            target_len +=1
        l,r=0,0
        sub_str={}
        while r < len(s2):
            if(target_len>=r-l+1):
                if s2[r] in sub_str:
                    sub_str[s2[r]]+=1
                else:
                    sub_str[s2[r]]=1
                r+=1
            else:
                sub_str[s2[l]] -=1
                if(sub_str[s2[l]] == 0):
                    del sub_str[s2[l]]
                l+=1
            if(sub_str==target):
                return True
        return False