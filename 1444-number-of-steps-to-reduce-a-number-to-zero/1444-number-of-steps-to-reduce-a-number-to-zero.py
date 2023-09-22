class Solution:
    def numberOfSteps(self, num: int) -> int:
        def fun(n,c):
            if n==0: return c
            if n%2==0:
                return fun(n//2,c+1)
            else:
                return fun(n-1,c+1)
        return fun(num,0)