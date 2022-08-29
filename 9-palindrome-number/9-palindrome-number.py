class Solution:
    def isPalindrome(self, x: int) -> bool:
        tNum = str(x)
        l, r = 0, len(tNum)-1
        while l <= r:
            if tNum[l] != tNum[r]:
                return False
            l += 1
            r -= 1
        return True

        