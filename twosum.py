#this is my code    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
#which is one of the slowest method to solve the porblem