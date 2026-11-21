class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hsh = {}
        for c in s:
            if (c in hsh):
                hsh[c]+=1
            else:
                hsh[c]=1
        for c in t:
            if(c not in hsh):
                return False
            else:
              hsh[c]-=1
        for x in hsh.values():
            if (x!=0):
                return False
        return True