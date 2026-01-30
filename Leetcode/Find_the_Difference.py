class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)): #taking s since it is shorted to avoid "out of index" error
            if s[i] != t[i]:
                return t[i]
        return t[-1] #extra character at the end
