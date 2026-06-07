class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=[]
        nums.sort()
        for i, val in enumerate(nums): 
            if val > 0:
                break
            if i > 0 and val==nums[i-1]:
                continue
            target = -nums[i]
            l = i+1
            u = len(nums)-1
            while(l < u):
                value = nums[l] + nums[u]
                if(value > target):
                    u -=1
                if(value < target):
                    l +=1
                if value == target:
                    result.append([nums[i],nums[l],nums[u]])
                    l+=1
                    u-=1
                    while nums[l] == nums[l-1] and l<u:
                        l+=1
        return result

