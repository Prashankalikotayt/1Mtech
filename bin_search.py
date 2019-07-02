#Binary Search 
#Prashant Kalikotay
import math
arr=[34,56,60,66,70,80,93];			#initialising a sorted array
print "these is the list where you have to search"
print arr
print "enter the element you want to find"      
x=input()					#element we want to find
l=0						#intialising l=0 to access the first element in the list
h=len(arr)-1					#initialising h=len(arr)-1 last element of the list
m=(h+l)/2					#middle element it does flooring
						#loop invariant: array is sorted anytime,l'<h' anytime and element if x belongs to arr then x always belongs to a[l,r]	
while l!=h:					#bound function is h-l  and terminating condition
	m=int(math.ceil((h+l)/2.0))		#taking ceiling
	if arr[m]<=x: 							
		   l=m 				#progress made by changing value of l and h after each iteration
	elif arr[m]>x:
		   h=m-1
if arr[l]==x:	
	print"element found","with position",m+1,""
else: 
	print"element not found"

#----------------------B.E.A.N------------------------------------#

#Boundary Case: when n=0 and n=1 we have boundary case.
#Exception Case: when user input is a negative number or characters
#Alternative Case: If the element to search is not there in the list.




	     	
