class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet=set()
        l,res=0,0
        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l+=1
            cSet.add(s[r])
            res=max(res,r-l+1)
        return res
        