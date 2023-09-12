class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res=[]
        size_duplicate={}
        if not groupSizes: return res
        for i,size in enumerate(groupSizes):
            if size not in size_duplicate:
                size_duplicate[size]=[]
            size_duplicate[size].append(i)
            if len(size_duplicate[size])==size:
                res.append(size_duplicate[size])
                size_duplicate[size]=[]
        return res