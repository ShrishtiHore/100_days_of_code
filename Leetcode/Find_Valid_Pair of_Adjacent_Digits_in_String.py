class Solution:
    def findValidPair(self, s: str) -> str:
        freq = {} #dictionary

        # count frequency
        for ch in s:
            #dict.get(key, default) so give me current value as key and if not provide default as zero
            #then increment the count becoz we have seen this count one more time
            freq[ch] = freq.get(ch, 0) + 1

        # check adjacent pairs
        for i in range(len(s) - 1):
            # the conditions for valid pair are:
            # 1. the current digit and the next digit are different
            # 2. the current digit appears exactly as many times as its value
            # 3. the next digit also appears exactly as many times as its value
            if (
                s[i] != s[i + 1]
                and freq[s[i]] == int(s[i])
                and freq[s[i + 1]] == int(s[i + 1])
            ):
                return s[i] + s[i + 1]
            
        return ""

