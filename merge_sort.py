#merge sort using recursion
#Prashant Kalikotay
def mergesort(a,l,r):
	if l<r:				#bound function is r-l,base case here is sorting 2 elements
		m=(l+r)/2   		#initialising middle element taking floor
		mergesort(a,l,m)	#recursive calling for first half elements: Progress
		mergesort(a,m+1,r)      #recursive calling for second half elements progressing step
		merge(a,l,m,r)		#merging elements after sorting, progressing step   

def merge(a,l,m,r):			# merge function
	p=m-l+1				#initialising p as the number of elements to be present in left array
	s=r-m				#initialising p as the number of elements to be present in right array
	L=[0]*(p)			#initialising left list as all 0's
	R=[0]*(s)			#initialising right list as all 0's
	for i in range(0,p):		
		L[i]=a[l+i]		#copying elements	
	for j in range(0,s):
		R[j]=a[m+1+j]	
	i=0				
	j=0
	k=l
	while i<p and j<s:		
		if(L[i]<=R[j]):
			a[k]=L[i]
			i+=1
		else:
		 	a[k]=R[j]
			j+=1
		k+=1
	while i<p:
		a[k]=L[i]
		i+=1
		k+=1
	while j<s:
                a[k]=R[j]
                j+=1
                k+=1
		
print "How many elements do you wish to enter in the list:"
n=input()
i=0
a=[]
l=0					#first elwment of the list
print"enter elements in the list"
while i<n:
	a.append(input())
	i+=1
r=len(a)-1				#last element of the list
mergesort(a,l,r)			#main function call
print a
#----------------------B.E.A.N------------------------------------#

#Boundary Case: when n=0 and n=1 we have boundary case.
#Exception Case: when user input is a negative number or characters.
#Alternative Case: When the user input is already a sorted array.


















