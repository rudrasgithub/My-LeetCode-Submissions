class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        st=set()
        for i in range(n):
            for j in range(i+1,n):
                hashset=set()
                for k in range(j+1,n):
                    sum=nums[i]+nums[j]+nums[k]
                    fourth=target-sum
                    if fourth in hashset:
                        temp=[nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        st.add(tuple(temp))
                    hashset.add(nums[k])
        ans=list(st)
        return ans