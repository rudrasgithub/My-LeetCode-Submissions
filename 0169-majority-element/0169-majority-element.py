class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        for i in nums:
            if c==0:
                ele=i
                c=1
            elif ele!=i:
                c-=1
            else:
                c+=1
        cnt=0
        for i in nums:
            if i==ele:
                cnt+=1
        if cnt>n//2: return ele