#SIEVE OF ERATOSTHENES
#PRASHANT KALIKOTAY
count=0
print"enter the value of n"
n=input()
a=[1 for i in range(n)]
for j in range (2,n):
	if(a[j]==1):
		for k in range(j,n):
			c=j*k
			if(c<n):
				a[c]=0

for i in range (2,n):
	if(a[i]==1):
		count+=1
		print i
 	  
print count
#----------------------B.E.A.N------------------------------------#

#Boundary Case: when n=0 and n=1 we have boundary case.
#Exception Case: when user input is a negative number or characters
#Alternative Case: When user input is less than 4.

