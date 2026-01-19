class Solution:
    def longestCommonPrefix(self, strs):

        #if the list is empty there is nothing to compare so return empty string
        if not strs: 
            return ""

        #go by character by character in the first string of the array
        for i in range(len(strs[0])):
            char = strs[0][i] #pick the current character in the string. this is the character all other strings should match. 
            
            for s in strs: #Now check this character against every string in the list.
                if i == len(s) or s[i] != char: #checking failure cases: 1. string too short 2. character does not match
                    return strs[0][:i] #as soon as mismatch happens return everything before this index
                    
        return strs[0] #and if all matches return full string



strs = input("Enter strings separated by space: ").split()

sol = Solution()
print(sol.longestCommonPrefix(strs))
