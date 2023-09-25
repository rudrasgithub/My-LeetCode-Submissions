import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        mx=-sys.maxsize-1
        for i in range(len(nums)):
            s+=nums[i]
            if s>mx:
                mx=s
            if s<0:
                s=0
        return mx