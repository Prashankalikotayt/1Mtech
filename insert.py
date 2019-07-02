#inserting an element in the correct position
#Prashant Kalikotay 
print("Enter the number of elements:")
s=input()			#initialising s as the number of elements uder wants to enter
a=[]				#intialising a list a
print "enter elements:"		
for i in range(s):		#loop condition: enter s no. of elements
				#loop invariant: elements from a[0]to a[j-1] are  always sorted
	a.append(input())       #appending element to the list a
print "enter the value of x"
x=input()			#initialising x as the element which we want to insert
a.append(x)			#appending x to the list
i=0				# i=0 as we should check elements from the 0eth element of the list
j=len(a)-1			#j is initialised len(a)-1 because it would go out of bound in the list
while j>0:			#loop length of the list is more than 0. Bound function is j here.
	if(a[j]<a[j-1]):        #checking for swapping
		temp=a[j]       #swapping
		a[j]=a[j-1]	#swapping
 		a[j-1]=temp	#swapping
		j-=1            #progress by decrementing the position of j varialble
	else: break            
print a                         #printing the list

#----------------------B.E.A.N------------------------------------#

#Boundary Case: Where the list has 0 elements
#Exception Case: when user input is a character
#Alternative Case:when we do not have a list where user can insert an element. 



