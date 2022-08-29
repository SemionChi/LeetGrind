class Solution:
    def romanToInt(self, s: str) -> int:
        tArr=[]
        res=0
        romanDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        for i in range(len(s)):
            tArr.append(romanDict[s[i]])
        for i in range(len(tArr)):
            if i==0:
                res+=tArr[i]
                continue
            if tArr[i]==tArr[i-1]:
                res += tArr[i]
                continue
            elif tArr[i]>tArr[i-1]:
                res += tArr[i]
                res -= 2* tArr[i-1]
            else:
                res += tArr[i]
                continue
        return(res)