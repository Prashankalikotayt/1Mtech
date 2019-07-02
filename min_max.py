#finding minimum and maximum in an array
#Prashant Kalikotay
def min_max(a,l,u):
	m=(l+u)/2;				#initialising the middle element
	send=[]						
	recv1=[]
	recv2=[]
	if((u-l)<=1):				#induction: Base case if there is only one element left between indexes l and u	
		if(a[l]<a[u]):
			send.append(a[l])
			send.append(a[u])
		        return (send)	
		else:
			send.append(a[u])
			send.append(a[l])
			return send
			
	else:
	 	recv1=min_max(a,l,m)		#progress made by recursive calling for first half of the list
		recv2=min_max(a,m+1,u)		#progress made by recursive calling for second half of the list
   	if(recv1[0]>recv2[0]):			#termination case.	
		recv1[0]=recv2[0]	
   	if(recv1[1]<recv2[1]):
		recv1[1]=recv2[1]
        return recv1

print "enter the number of elements:"
n=input()					
print "enter the values in the list for which you want to check minimum and maximum:"
a=[]
l=0;						#initialisation first element index
final=[]
for i in range(0,n):				#loop for taking input in the list
	a.append(input())			
u=len(a)-1					#initialisation last element index
final=min_max(a,l,u)				#function call for finding min and max in the list
print "max=",final[1],"\n", "min:",final[0],"\n"  #printing the final output	
#----------------------B.E.A.N------------------------------------#

#Boundary Case: when n=0 and n=1 we have boundary case.
#Exception Case: when user input is a negative number or characters
#Alternative Case: When we have only 1 element in the list.

	
