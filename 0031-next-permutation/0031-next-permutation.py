class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        idx=-1
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                idx=i
                break
        if idx==-1:
            arr.reverse()
            return arr
        for i in range(n-1,idx,-1):
            if arr[i]>arr[idx]:
                arr[i],arr[idx]=arr[idx],arr[i]
                break
        arr[idx+1:]=reversed(arr[idx+1:])
        return arr