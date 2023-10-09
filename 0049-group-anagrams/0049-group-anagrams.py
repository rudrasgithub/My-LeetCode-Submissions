class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap=defaultdict(list)
        for word in strs:
            anagram=''.join(sorted(word))
            hashMap[anagram].append(word)
        ans=list(hashMap.values())
        return ans