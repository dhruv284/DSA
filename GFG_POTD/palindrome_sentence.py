class Solution:
	def isPalinSent(self, s):
		# code here
		
		i=0
		j=len(s)-1
		
		while(i<=j):
		    if s[i].isalnum()==False:
		        i+=1
		        continue
		    if s[j].isalnum()==False:
		        j-=1
		        continue
		    if s[i].isalnum()==True and s[j].isalnum()==True:
		        if s[i].lower()==s[j].lower():
		            j-=1
		            i+=1
		        else:
		            return False
		    
		return True