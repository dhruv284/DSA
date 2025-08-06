class Solution:
    def romanToDecimal(self, s): 
        # code here
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        tot=0
        for i in range(len(s)):
            if i==len(s)-1:
                tot+=dic[s[i]]
            elif dic[s[i]]<dic[s[i+1]]:
                tot-=dic[s[i]]
            else:
                tot+=dic[s[i]]
        return tot