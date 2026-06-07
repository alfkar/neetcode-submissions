class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared_numbers = {}
        for num in nums:
            if(appeared_numbers.get(num)):
                return True
            else:
                appeared_numbers[num]=1
        return False

