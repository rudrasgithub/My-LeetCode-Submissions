class Solution:
    def myPow(self, x: float, n: int) -> float:
        power=n
        ans=1
        if n<0: power*=-1
        while power>0:
            if power%2==0:
                x=x*x
                power//=2
            else:
                ans*=x
                power-=1
        if n<0: ans=1/ans
        return ans