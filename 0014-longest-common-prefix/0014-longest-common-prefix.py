class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        n=len(s)
        if n==0: return ""
        if n==1: return s[0]
        c=0
        i=0
        s.sort()
        mn=min(len(s[0]),len(s[n-1]))
        while i<mn and s[0][i]==s[n-1][i]:
            c+=1
            i+=1
        lcp=s[0][:c]
        return lcp