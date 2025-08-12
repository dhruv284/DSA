class Solution:
    def minDifference(self, arr):
        # code here
        
        for i in range(len(arr)):
            arr[i]=(int(arr[i][0:2])*60*60+int(arr[i][3:5])*60+int(arr[i][6:9]))
            
        diff=float('inf')
        arr.sort()
        for i in range(len(arr)-1):
            diff=min(abs(arr[i]-arr[i+1]),diff)
        secdiff=86400-arr[len(arr)-1]+arr[0]
        diff=min(diff,secdiff)
        return diff