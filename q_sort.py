#quick_sort
#Author Prashant K
#Date:25/06/2018
def part(a,l,u):		# this function finally takes the last element to its correct position 
	x=a[u]			#last element is used for partition 
	j = u-1
	i = l
	while i<=j:		#bound function is j-i	
		if a[i]<=x:
			i=i+1	
		elif a[j]>x:
			j=j-1
		else:
			a[i],a[j] = a[j],a[i]    #swapping elements
			i+=1			 # progress and maintenance	
			j-=1			 # progress and maintenance		
	a[u],a[i]=a[i],a[u]
	print(a)
	return i				


def q_sort(a,l,h):
  if l<h:
	pivot=part(a,l,h)
	q_sort(a,l,pivot-1)
	q_sort(a,pivot+1,h)

print("Enter the number of elements:")
s=input()                        #initialising s as the number of elements user wants to enter
a=[]                             #intialising a list a
print "enter elements:"
for i in range(s):               #loop condition: enter s no. of elements
        a.append(input())        #appending element to the list a
l=0                             #i=0 as we should check elements from the 0eth element of the list
u=len(a)-1                
print("A = ",a)
q_sort(a,l,u)
print(part(a,l,u))
print("sorted = ",a)
#----------------------B.E.A.N------------------------------------#

#Boundary Case: when n=0 and n=1 we have boundary case.
#Exception Case: when user input is a negative number or characters
#Alternative Case: When the user input is already a sorted array.

