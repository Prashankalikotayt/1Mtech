#reversing the strings
print("Enter a string you want to reverse:")
str1=raw_input()	#taking the string input
a=list(str1)		#putting each element of the string in  a list
i=0			#initialising i to 0 as we have to access the list from it's first element
temp=''			#temporary string variable 
j=len(str1)-1		# j initialised to total_length-1 as it may go out of bound
n=j			# n is initialised as the length of string
while i<=(n/2):		#loop condition: it should run for half the length of the string,loop invariant: i index gives us the number of swaps made. Bound function is len(string)/2 -i
        temp=a[i]	#swapping
	a[i]=a[n-i]
 	a[n-i]=temp	
	i+=1  		#progress by incrementing i
	
str2="".join(a)		#joining each element of the list as a string
print str2
#----------------------B.E.A.N------------------------------------#

#Boundary Case: when n=0 we have boundary case.
#Exception Case: when user input is a number. 
#Alternative Case:When user input is has all same characters or the input is a palindrome.
