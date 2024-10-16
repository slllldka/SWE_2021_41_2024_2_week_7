from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    d = dict()
    i = 0
    for e in nums:
        d[e] = i
        i = i+1
    i = 0
    for e in nums:
        diff = target - nums[i]
        if diff in d:
            if d[diff] > i:
                return [i, d[diff]]
        i = i+1
        
 # Your Codes
 ## Do not use input() or print() in your function
 ## Inputs (nums, target) will given as arguments and the output as 
## return value
## return # Your Answer