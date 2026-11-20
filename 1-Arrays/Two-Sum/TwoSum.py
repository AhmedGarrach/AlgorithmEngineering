class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap={}
        for i,x in enumerate(nums):
            other = target - x
            if (other in hashmap):
                return [hashmap[other],i]
            hashmap[x]=i