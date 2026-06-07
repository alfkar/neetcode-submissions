class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        lower = 0
        upper = 1
        if(len(numbers) < 2):
            return [0,0]
        while(True):
            val_sum = numbers[lower] + numbers[upper]
            if val_sum== target:
                return [lower+1, upper+1]
            if((val_sum < target)):
                upper +=1
                if(upper < len(numbers)):
                    continue
            lower +=1
            upper = lower+1

