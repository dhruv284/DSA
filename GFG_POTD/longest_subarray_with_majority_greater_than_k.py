
#User function Template for python3
class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        mp={}
        mp[0]=-1
        l=0
        sum1=0
        for i in range(len(arr)):
            if arr[i]>k:
                sum1+=1
            else:
                sum1-=1
            
            if sum1>0:
                l=max(l,i+1)
            if (sum1-1) in mp:
                l=max(l,i-mp[sum1-1])
            if (sum1) not in mp:
                mp[sum1]=i
        return l