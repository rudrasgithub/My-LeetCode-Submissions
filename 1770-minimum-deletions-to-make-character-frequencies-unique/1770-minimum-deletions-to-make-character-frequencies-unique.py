class Solution:
    def minDeletions(self, s: str) -> int:
        HashMap=Counter(s)
        deletions=0
        check_duplicate=set()
        for char,freq in HashMap.items():
            while freq>0 and freq in check_duplicate:
                freq-=1
                deletions+=1
            check_duplicate.add(freq)
        return deletions