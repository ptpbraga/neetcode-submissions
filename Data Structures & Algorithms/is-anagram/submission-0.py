class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        rep_t ={}
        rep_s = {}
        for i in s:
            if i not in rep_s:
                rep_s[i]=0
            rep_s[i]+=1
        for i in t:
            if i not in rep_t:
                rep_t[i]=0
            rep_t[i]+=1

        if rep_s == rep_t:
            return True;
        else:
            return False;

        