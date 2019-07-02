#partioning the elements in the list. Given an element x.
print("Enter the number of elements:")
s=input()     			 #initialising s as the number of elements user wants to enter
a=[]				 #intialising a list a
print "enter elements:"
for i in range(s): 		 #loop condition: enter s no. of elements
	a.append(input())	 #appending element to the list a
print "enter the value of x"
i=0                             # i=0 as we should check elements from the 0eth element of the list
j=len(a)-1			#j is initialised len(a)-1 because it would go out of bound in the list
x=a[j]
while i<j:		        #loop length of the list is more than 0. Bound function is j-i
	if a[i]<x:		#condition for checking if the element is greater than the ith element
		i+=1 	 	#progress by incrementing i	
	elif a[j]>x:		#condition for checking if the jth element of the array is greater than x
		j-=1		#progress by decrementing j
	else:			#default case swapping 
		temp=a[i]
		a[i]=a[j]
 		a[j]=temp	
print a
#----------------------B.E.A.N------------------------------------#

#Boundary Case: when n=0 and n=1 we have boundary case.
#Exception Case: when user input is a negative number or characters
#Alternative Case:When the list is sorted
