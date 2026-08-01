a=int(input("Enter the marks of Python Programming :"))
b=int(input("Enter the marks of SE :"))
c=int(input("Enter the marks of DBMS :"))
d=int(input("Enter the marks of DSA :"))
e=int(input("Enter the marks of PAI :"))
total=a+b+c+d+e
percent=((total*100)/500)
z=float(percent)
if(z>=90):
	print("The grade is A and Percentage is:",z)
elif (z>80):
	print("The grade is B and Percentage is:",z)
elif(z>70):
	print("The grade is C and percentage is:",z)
elif (z>60):
	print("The grade is D and percentage is:",z)
else:
	print("The Student is Fail,z")
