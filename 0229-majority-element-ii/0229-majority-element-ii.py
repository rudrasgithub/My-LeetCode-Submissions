class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        c1=c2=0
        ele1=ele2=float('inf')
        for i in nums:
            if c1==0 and i!=ele2:
                ele1=i
                c1=1
            elif c2==0 and i!=ele1:
                ele2=i
                c2=1
            elif i==ele1:
                c1+=1
            elif i==ele2:
                c2+=1
            else:
                c1-=1
                c2-=1
        c1=c2=0
        for i in nums:
            if i==ele1:
                c1+=1
            elif i==ele2:
                c2+=1
        ans=[]
        if c1>n//3:
            ans.append(ele1)
        if c2>n//3:
            ans.append(ele2)
        return ans