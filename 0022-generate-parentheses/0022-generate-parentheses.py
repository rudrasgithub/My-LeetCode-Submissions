class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(n,s,open,close,ans):
            if close==n:
                ans.append(s)
                return
            else:
                if open<n:
                    generate(n,s+"(",open+1,close,ans)
                if open>close:
                    generate(n,s+")",open,close+1,ans)
        ans=[]
        generate(n,"",0,0,ans)
        return ans