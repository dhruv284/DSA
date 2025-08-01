class Solution:
    def countBalanced(self, arr):
        # code here
        
        mp={}
        prefdiff=0
        mp[prefdiff]=1
        res=0
        for i in range(len(arr)):
            vowels=0
            conso=0
            for x in arr[i]:
                if x=="e" or x=="a" or x=="i" or x=="o" or x=="u":
                    
                    vowels+=1
                else:
                    conso+=1
            prefdiff+=vowels-conso
            if prefdiff in mp:
                res+=mp[prefdiff]
                mp[prefdiff]+=1
            else:
                mp[prefdiff]=1
        return res