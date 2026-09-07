class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

       if len(s)!= len(t):
        return False

       h1 = dict() 
       h2 = dict()
       for ch in s:
        if ch in h1.keys():
            x = h1[ch]
            h1[ch] = x+1
        else :
            h1[ch]=1

       for ch in t :
        if ch in h2.keys():
            x = h2[ch]
            h2[ch] = x+1
        else :
            h2[ch]=1

       for ch in h1.keys():
        # if the char is only missing
        if ch not in h2.keys():
            return False
        # the frq of char occurence in both the strings are diff
        elif h1[ch]!= h2[ch] :
            return False

       return True 
        
    



         