#Euclid's Division Algorithm
#Prashant Kalikotay
b=input("Enter Divisor: ")	#initialising value of divisor
a=input("Enter Dividend: ")	#initialising value of dividend
r=a;				#remainder value is initialised as the value of dividend(as in the program we are decrementing at each step))
q=0;				# quotient is set to 0 initially
while (r>=b):			# loop: loop invariant is a=b*q+r & bound function is r-b
	r-=b			#progress is made here by decrementing r divisor times 
	q+=1 			#progress is made here by incrementing quotient by 1 
print "quotient:",q,"Remainder:",r,"\n" 
#----------------------B.E.A.N------------------------------------#

#Boundary Case: when n=0 and n=1 we have boundary case.
#Exception Case: when user input for divisor is 0.
#Alternative Case:When Dividend and Divisor are all 0.



