class Solution:
    def swap(self,arr1,arr2,ind1,ind2):
        if arr1[ind1]>arr2[ind2]:
            arr1[ind1],arr2[ind2] = arr2[ind2],arr1[ind1]
    def merge(self, arr1: List[int], n: int, arr2: List[int], m: int) -> None:
        len=n+m
        gap=(len//2)+len%2
        while gap>0:
            left=0
            right=gap
            while right<len:
                #arr1 and arr2
                if left<n and right>=n:
                    self.swap(arr1,arr2,left,right-n)
                #arr2 and arr2
                elif left>=n:
                    self.swap(arr2,arr2,left-n,right-n)
                #arr1 and arr1
                else:
                    self.swap(arr1,arr1,left,right)
                left+=1
                right+=1
            if gap==1: break
            gap=(gap//2)+gap%2
        arr1[n:]=arr2[:]