class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in range(len(nums)):
            nextEle=target-nums[i]
            if nextEle in hashMap:
                return [hashMap[nextEle],i]
            hashMap[nums[i]]=i
        return [-1,-1]